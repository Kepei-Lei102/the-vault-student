/* heap-lab.c — where a process's memory actually is, and what the heap costs.
 *
 * Build and run:  cc -O1 -o /tmp/heap-lab heap-lab.c && /tmp/heap-lab
 *
 * Part 1 prints the address of one thing from each region of the process:
 * the code, a global, a local on the stack, and blocks from the heap. The
 * numbers differ every run (address-space randomisation) but the ORDER and
 * the DIRECTIONS do not: the stack grows down, the heap grows up.
 * Part 2 times allocation on the stack against the heap.
 * Part 3 leaks on purpose and watches the process grow.
 * Part 4 frees a block and shows that the pointer still points at it.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/resource.h>

int a_global = 42;                       /* data segment */
static long rss_mb(void) { struct rusage r; getrusage(RUSAGE_SELF, &r);
#ifdef __APPLE__
    return r.ru_maxrss / (1024 * 1024);   /* bytes on macOS */
#else
    return r.ru_maxrss / 1024;            /* kilobytes on Linux */
#endif
}
static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec * 1e-9; }
static int deeper(int depth) { int local = depth; if (depth == 0) { printf("  local at depth 3    %p\n", (void *)&local); return local; } return deeper(depth - 1) + (int)(long)&local % 1; }

int main(void) {
    int a_local = 1;
    char *h1 = malloc(100), *h2 = malloc(100), *h3 = malloc(100000);
    printf("1. one address from each region (this run):\n");
    printf("  code  (main)        %p\n", (void *)main);
    printf("  data  (a_global)    %p\n", (void *)&a_global);
    printf("  heap  (malloc 100)  %p\n", (void *)h1);
    printf("  heap  (malloc 100)  %p   +%ld bytes from the first\n", (void *)h2, (long)(h2 - h1));
    printf("  heap  (malloc 100k) %p\n", (void *)h3);
    printf("  stack (a_local)     %p\n", (void *)&a_local);
    deeper(3);
    printf("  -> the stack address at depth 3 is LOWER than main's: the stack grows down; the heap grew up.\n\n");

    /* 2. cost: a stack allocation is a subtraction from the stack pointer; a heap allocation is a search plus
       bookkeeping, and a large one is a request to the operating system. Small blocks are kept alive until
       the end of each round so that the allocator cannot simply hand the same block straight back. */
    enum { N = 100000 };
    double t0 = now(); volatile long sink = 0;
    for (int round = 0; round < 20; round++)
        for (int i = 0; i < N; i++) { char buf[64]; buf[0] = (char)i; sink += buf[0]; }
    double t_stack = (now() - t0) / (20.0 * N) * 1e9;
    char **keep = malloc(N * sizeof *keep);
    t0 = now();
    for (int round = 0; round < 20; round++) {
        for (int i = 0; i < N; i++) { keep[i] = malloc(64); keep[i][0] = (char)i; sink += keep[i][0]; }
        for (int i = 0; i < N; i++) free(keep[i]);
    }
    double t_heap = (now() - t0) / (20.0 * N) * 1e9;
    t0 = now();
    for (int i = 0; i < 2000; i++) { char * volatile p = malloc(1 << 20); p[0] = (char)i; sink += p[0]; free(p); }
    double t_big = (now() - t0) / 2000 * 1e9;
    printf("2. allocate and free, per block:\n   64 bytes on the stack %.2f ns   64 bytes on the heap (%d live at once) %.1f ns   1 MB on the heap %.0f ns\n\n", t_stack, N, t_heap, t_big);

    /* 3. a leak: allocate and forget, and watch the process grow */
    long before = rss_mb(); unsigned long addr_sum = 0;
    for (int i = 0; i < 200000; i++) { char *p = malloc(1000); p[0] = 1; addr_sum += (unsigned long)p; /* never freed */ }
    printf("3. 200 000 blocks of 1000 bytes allocated and forgotten: resident memory %ld MB -> %ld MB (checksum %lx)\n\n", before, rss_mb(), addr_sum & 0xfff);

    /* 4. a dangling pointer: the block is freed, the pointer is not changed */
    char *name = malloc(16); strcpy(name, "alice");
    free(name);
    char *other = malloc(16); strcpy(other, "mallory");
    printf("4. after free(name) and a new malloc: name -> %p, other -> %p, same block: %s\n   reading through the stale pointer gives \"%s\" (undefined behaviour; today it is the new tenant)\n",
           (void *)name, (void *)other, name == other ? "yes" : "no", name);
    free(other);
    return (int)(sink & 1);
}
