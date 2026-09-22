/* modern-cpu-lab.c — three experiments that expose the engine behind the textbook CPU. Every number in
 * The Modern CPU vs the Textbook Model.md comes from running this on the machine named in the card.
 *
 *   cc -O1 -o modern-cpu-lab modern-cpu-lab.c && ./modern-cpu-lab
 *
 * 1. Branch prediction: the same loop over the same numbers, sorted and unsorted. The work is identical; only
 *    the predictability of one branch changes.
 * 2. Instruction-level parallelism: a million additions as one dependency chain, then the same million split
 *    across eight independent chains. Same instructions; the second lets the core run several at once.
 * 3. The memory wall: walking a 128 MB array in order, then following a random chain of pointers through it.
 *    Same number of loads; the second defeats the cache and the prefetcher.
 * Compiled at -O1 so the compiler keeps the branch as a branch; at -O2 clang replaces it with a conditional
 * move and experiment 1 shows nothing, which is itself a lesson and the card says so.                        */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>

static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec * 1e-9; }
static int cmp(const void *a, const void *b) { return (*(const int *)a > *(const int *)b) - (*(const int *)a < *(const int *)b); }

int main(void) {
    const int N = 1 << 20, REPS = 50;
    int *a = malloc(N * sizeof *a); srand(7);
    for (int i = 0; i < N; i++) a[i] = rand() & 255;

    /* 1. branch prediction: the branch body updates a small table through a computed address, so the compiler
     *    cannot replace the branch by a conditional move (at -O2 it does exactly that for a plain sum, and the
     *    two timings collapse together: the compiler has done the predictor's job for it).                    */
    long long hist[8] = {0};
    for (int pass = 0; pass < 2; pass++) {
        if (pass == 1) qsort(a, N, sizeof *a, cmp);
        long long sum = 0; double t0 = now();
        for (int r = 0; r < REPS; r++)
            for (int i = 0; i < N; i++) if (a[i] >= 128) { sum += a[i]; hist[a[i] & 7]++; }
        double dt = now() - t0;
        printf("branch  %-8s  %.3f s  (%.2f ns per element, sum %lld, hist[0] %lld)\n", pass ? "sorted" : "unsorted", dt, dt / ((double)N * REPS) * 1e9, sum, hist[0]);
    }

    /* 2. dependency chain against independent chains: floating-point additions, which the compiler may not
     *    reorder, over a small array that stays in the L1 cache.                                               */
    const int K = 4096; const long ROUNDS = 100000; double *x = malloc(K * sizeof *x); volatile double sink;
    for (int i = 0; i < K; i++) x[i] = (i % 7) * 0.25;
    { double t0 = now(); double s = 0; for (long r = 0; r < ROUNDS; r++) for (int i = 0; i < K; i++) s += x[i]; sink = s; double dt = now() - t0;
      printf("adds    1 chain   %.3f s  (%.3f ns per add)\n", dt, dt / ((double)K * ROUNDS) * 1e9); }
    { double t0 = now(); double s0 = 0, s1 = 0, s2 = 0, s3 = 0, s4 = 0, s5 = 0, s6 = 0, s7 = 0;
      for (long r = 0; r < ROUNDS; r++) for (int i = 0; i < K; i += 8) { s0 += x[i]; s1 += x[i+1]; s2 += x[i+2]; s3 += x[i+3]; s4 += x[i+4]; s5 += x[i+5]; s6 += x[i+6]; s7 += x[i+7]; }
      sink = s0 + s1 + s2 + s3 + s4 + s5 + s6 + s7; double dt = now() - t0;
      printf("adds    8 chains  %.3f s  (%.3f ns per add)\n", dt, dt / ((double)K * ROUNDS) * 1e9); }
    free(x);

    /* 3. the memory wall: sequential walk against a random pointer chase */
    const size_t W = (size_t)1 << 24;                       /* 16M entries × 8 B = 128 MB */
    size_t *next = malloc(W * sizeof *next);
    for (size_t i = 0; i < W; i++) next[i] = (i + 1) % W;   /* sequential ring */
    { size_t p = 0; double t0 = now(); for (size_t i = 0; i < W; i++) p = next[p]; sink = (double)p; double dt = now() - t0;
      printf("memory  sequential  %.3f s  (%.2f ns per load)\n", dt, dt / W * 1e9); }
    for (size_t i = W - 1; i > 0; i--) { size_t j = ((size_t)rand() * 65536 + rand()) % (i + 1); size_t t = next[i]; next[i] = next[j]; next[j] = t; }
    { size_t p = 0; double t0 = now(); for (size_t i = 0; i < W; i++) p = next[p]; sink = (double)p; double dt = now() - t0;
      printf("memory  random      %.3f s  (%.2f ns per load)\n", dt, dt / W * 1e9); }
    free(a); free(next); return 0;
}
