---
chinese: Java 的数组与 ArrayList (Java de shùzǔ yǔ ArrayList)
prerequisites:
  - "[[Java Classes]]"
  - "[[Arrays]]"
  - "[[Searching]]"
  - "[[Sorting]]"
leads_to: []
tags:
  - subject/computer-science
  - domain/programming
  - domain/java
  - domain/data-structures
  - level/A-Level
  - level/pre-AP
  - curriculum/AP-CSA
  - curriculum/Cambridge-9618
  - curriculum/IB-CS
  - type/companion
  - type/language-reference
  - misconception/removing-while-traversing-forward-is-safe
  - misconception/the-enhanced-for-variable-is-the-element
  - misconception/arraylist-uses-length-and-brackets
  - misconception/two-integers-compare-with-double-equals
  - misconception/a-2d-array-is-a-grid
---

# Java Arrays and ArrayList Java 的数组与 ArrayList

> Remove every 8 from `[3, 8, 8, 8, 5]` with the obvious loop, `for (int i = 0; i < a.size(); i++) { if (a.get(i) == 8) { a.remove(i); } }`, and one 8 survives.
>
> Nothing threw an exception and nothing looked wrong. The list closed the gap behind the loop's back.

## What this is for

[[Arrays]] teaches what an array is and why indices start at zero; [[Searching]] and [[Sorting]] teach the algorithms; [[Java Classes]] taught you to write the classes whose objects will now be collected. This is the last of the Java companions, and it covers the largest unit of the course: arrays, text files, wrapper classes, `ArrayList`, 2D arrays, and the Java forms of the searches and sorts. Nothing here re-teaches an idea; every section is what Java does with an idea you already own.

Every program below is a real file in the folder `java-arrays-and-arraylist`, and every output shown came from compiling and running it. Run `python3 run_all.py` there to reproduce all of it.

**The one idea to carry through:** an array's length is fixed when it is made and its slots are numbered from `0` to `length - 1`; an `ArrayList` grows and shrinks, and **every insertion or removal renumbers everything after it**. Most array bugs are a count that started at one; most list bugs are an index written down before the list moved.

## 中文锚点

电影院的座位是钉在地上的，一排一排都有编号。每个座位有自己的号，数一数就能马上找到，电影票卖光了，谁也没法再添一个座位。婚宴的桌子摆法就不一样：客人多了可以加桌，来晚的人可以挤到两个朋友中间去坐，可这样一来，那一边排在后面的每一个人都得往后挪一个位子；要是挪动之前你在卡片上写了“左起第三个”，现在这张卡片指的就是另一个人了。这就是 Java 用一个名字装下许多个值的两种办法。数组是电影院：格子的数目是固定的，造出来的时候就定了，按编号去找，永远不能加长。ArrayList 是婚宴的桌子：一边加一边长，可以往中间放东西，也可以从中间拿走东西，而每做一次，后面所有东西的编号都得跟着挪一位。用列表出的错，多半是忘了最后这句话；用数组出的错，多半是座位明明从零开始编号，人却从一开始数。

## 1. A data set is a collection you walk through one value at a time

Marks for a class, temperatures for a week, pixels of an image: a **data set** is many values of one kind, and every question about it (the highest, the average, how many pass, whether two are equal) is answered by visiting the values one at a time and keeping a running answer. Before writing the loop it helps to draw the data as a row of boxes, or a table for two dimensions, and to say in words what the running answer is. Everything below is that plan, in Java, for its two containers.

## 2. Arrays: fixed length, numbered from zero

```java
int[] marks = new int[4];                    // length fixed for ever; every slot at the default 0
String[] names = new String[2];              // a reference type: every slot is null
marks[0] = 71;                               // [] to write ...
System.out.println(marks[3] + " length " + marks.length);   // ... and to read; .length has no brackets
int[] primes = {2, 3, 5, 7, 11};             // an initializer list: length 5, no new needed
```

From `ArrayBasics.java`: the defaults print as `0 0.0 false null`, the same defaults as a class's fields in [[Java Classes]]. `marks.length` is an **attribute**, written without brackets; `String` has `length()` with brackets, and the two are confused in every class. The last legal index is `length - 1`, and `primes[5]` on a five-element array stops the program:

```
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 5
```

An array is an object, so `int[] alias = primes;` copies the reference, and `alias[0] = 99` changes `primes[0]`: the aliasing of [[Java Objects, References and Strings]], now with a container.

### Two ways to traverse

```java
for (int i = 0; i < temps.length; i++) {     // indexed: you know WHERE you are
    System.out.print(i + ":" + temps[i] + " ");
}
for (int t : temps) {                        // enhanced for: "for each t in temps"
    System.out.print(t + " ");
}
```

The **enhanced for loop** hands you a **copy** of each element in turn and never its index. That has two consequences, both in `Traversals.java`:

- **Assigning to the loop variable changes nothing.** `for (int t : temps) { t = 0; }` leaves `temps` as it was; the indexed loop `temps[i] = 0` empties it.
- **For an array of objects, the copy is a copy of the reference**, so calling a method through it changes the object: `for (Tally t : tallies) { t.bump(); }` bumps every tally. Re-pointing the copy, `t = new Tally(100)`, changes nothing in the array.

Use the enhanced form to *read*; use the indexed form when you need the position, when you write to slots, or when you visit pairs of neighbours. Any enhanced loop can be rewritten as an indexed one.

### The standard array algorithms

All in `ArrayAlgorithms.java`, on `a = {4, 9, 2, 9, 7}`.

| Question | Running answer | Note |
|---|---|---|
| maximum | `int max = a[0];` then replace when bigger | start with the first element, never with 0 |
| sum, mean | `sum += x;` then `(double) sum / a.length` | cast before dividing |
| at least one has a property | `boolean any = false;` a find sets `true` | never set it back |
| all have a property | `boolean all = true;` a failure sets `false` | the mirror image |
| how many have a property | `count++` under an `if` | |
| consecutive pairs | compare `a[i]` with `a[i + 1]` for `i` up to `length - 2` | the classic off-by-one |
| duplicates | `for i` and `for j = i + 1` | each pair once |
| shift left | `shifted[i] = a[i + 1]`; the last slot keeps its default | |
| rotate left | `rotated[i] = a[(i + 1) % a.length]` | the `%` wraps the first element to the end |
| reverse in place | swap `a[i]` with `a[a.length - 1 - i]` for `i < a.length / 2` | walk to the middle |

The results: `max 9, sum 31, mean 6.2`; `2 rises`; `duplicate? true`; `[9, 2, 9, 7, 0]` shifted and `[9, 2, 9, 7, 4]` rotated; `[7, 9, 2, 9, 4]` reversed.

## 3. Reading a text file

A file keeps data when the program is not running. Java reads one with the same `Scanner` that read the keyboard in [[Java Objects, References and Strings]], now built round a `File` (`ReadFile.java`, on a file `marks.txt` holding `Ada 71`, `Bob 58`, `Cyd 92`):

```java
import java.io.File;                         // File and IOException live in java.io
import java.io.IOException;
import java.util.Scanner;

public static void main(String[] args) throws IOException {        // "if the file cannot be opened, stop"
    Scanner in = new Scanner(new File("marks.txt"));
    while (in.hasNext()) {                                         // is there anything left to read?
        String name = in.next();                                   // the next word
        int mark = in.nextInt();                                   // the next int
        ...
    }
    in.close();
}
```

`hasNext()` as the loop condition is the file-reading idiom. `next()` reads a word, `nextInt()` and `nextDouble()` a number (and throw `InputMismatchException` if the text is not one), `nextLine()` a whole line. A line is often cut into pieces with **`split`**: `"Ada 71".split(" ")` is the `String` array `{"Ada", "71"}`, and `ReadFile.java` uses it to print `A71 B58 C92`. Two rules: `throws IOException` on the header of any method that opens a file, and `close()` when finished. Open a file that is not there and the program stops with `FileNotFoundException`.

**Do not mix `nextLine()` with the other `next` methods on one file.** They treat line breaks differently, and the course description puts that combination out of scope for exactly that reason.

## 4. Wrapper classes: `int` as an object

A collection in Java holds objects, not primitives. So there is a class `Integer` that holds one `int`, and a class `Double` that holds one `double`, both in `java.lang` and both **immutable**. The compiler converts for you (`Wrappers.java`):

```java
ArrayList<Integer> scores = new ArrayList<Integer>();
scores.add(90);                              // autoboxing: the int 90 becomes an Integer object
int first = scores.get(0);                   // unboxing: the Integer becomes an int
int total = scores.get(0) + scores.get(1);   // unboxed for the +
```

**Autoboxing** happens when a primitive is passed where an object is expected or assigned to a wrapper variable; **unboxing** in the reverse cases. `Integer.parseInt` and `Double.parseDouble` are the class methods that turn text into numbers. One trap follows from `Integer` being an object: `==` compares references. Two `Integer`s holding `1000` give `a == b` **false** and `a.equals(b)` true. Two holding `100` give `true` for both, because small values happen to be shared, which makes the mistake survive small tests. Compare wrapped numbers with `equals`, or unbox them first.

## 5. ArrayList: the list that grows

```java
import java.util.ArrayList;                  // java.util, so it must be imported

ArrayList<String> queue = new ArrayList<String>();      // empty; grows as needed
queue.add("Ada");  queue.add("Bob");  queue.add("Cyd");
queue.add(1, "Dee");                                    // insert at index 1: Bob and Cyd move right
```

`ArrayList<E>` is **generic**: the `E` in the angle brackets is the type of every element, and writing it lets the compiler catch a wrong type before the program runs. `ArrayList<int>` is refused (`WrongType.java`: `error: unexpected type, required: reference, found: int`); write `ArrayList<Integer>`.

The six methods on the exam's reference sheet, from `ListBasics.java`:

| Call | Does | Returns | Indices after it |
|---|---|---|---|
| `size()` | how many | `int` | |
| `add(obj)` | appends | `true` | |
| `add(index, obj)` | inserts; `0 <= index <= size()` | nothing | everything from `index` on moves **right** |
| `get(index)` | reads | the element | |
| `set(index, obj)` | replaces | **the old element** | |
| `remove(index)` | deletes | **the removed element** | everything after it moves **left** |

![[java-arrays-list-shift.svg|820]]

After `add(1, "Dee")`, `set(2, "Bea")` (which returns `Bob`) and `remove(0)` (which returns `Ada`), the list is `[Dee, Bea, Cyd]`. Legal indices are `0` to `size() - 1`, and `get(3)` on three elements stops the program with `IndexOutOfBoundsException`. The vocabulary differs from arrays in exactly the ways that cause compile errors: `size()` not `length`, `get(i)` not `[i]`, and an `import`.

### Traversing a list, and the trap in the opening

Both loops work on lists: `for (int i = 0; i < nums.size(); i++) { nums.get(i) }` and `for (int n : nums)`. The danger is **removing while traversing**. `ListTraversal.java` removes every `8` from `[3, 8, 8, 8, 5]` four ways:

![[java-arrays-skip-on-remove.mp4]]

```
forward:  [3, 8, 5]      remove(1) slides the next 8 into index 1, and i++ steps over it
backward: [3, 5]         what slides is already behind i
careful:  [3, 5]         a while loop that advances i only when it did not remove
```

The fourth way, removing inside an **enhanced for**, stops the program with `ConcurrentModificationException`: the list's size changed under a loop that was not told. So: **never add or remove inside an enhanced for loop**, and when removing by index, walk backwards or advance only after a pass that removed nothing.

### The standard list algorithms

The array algorithms all carry over with `size()` and `get(i)` in place of `length` and `[i]`, and two are new because a list can change size (`ListAlgorithms.java`):

```java
int pos = 0;                                              // insert x keeping the list sorted
while (pos < sorted.size() && sorted.get(pos) < x) {      // the size() check comes first: short-circuit
    pos++;
}
sorted.add(pos, x);                                       // [2, 5, 9, 14] with 7 becomes [2, 5, 7, 9, 14]

int k = 0;                                                // delete every "tea"
while (k < words.size()) {
    if (words.get(k).equals("tea")) { words.remove(k); } else { k++; }
}                                                         // [tea, milk, tea, jam] becomes [milk, jam]
```

Two lists are often walked together with one index: the dot product of `[1, 2, 3]` and `[10, 20, 30]` is `140`. Reversing a list in place uses `set` for the swap, since `get` returns a value and cannot be assigned to.

## 6. Two dimensions: an array of arrays

```java
int[][] g = new int[2][3];                              // 2 rows of 3: every cell 0
int[][] m = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };        // an initializer list of rows
m[1][2] = 7;                                            // [row][col]
```

A 2D array is a 1D array whose elements are 1D arrays. That one fact gives every rule in `Grid.java`: `m.length` is the number of rows, `m[0].length` the number of columns, `m[1]` is a whole row (and `int[] middle = m[1]; middle[0] = 40;` changes `m[1][0]`, because it is a reference), and the exam's convention is **first index row, second index column**. The course keeps to rectangular grids.

Two traversals, and a third with the enhanced loop:

```java
for (int r = 0; r < m.length; r++) {                    // row-major: across each row
    for (int c = 0; c < m[r].length; c++) { ... m[r][c] ... }
}
for (int c = 0; c < m[0].length; c++) {                 // column-major: down each column
    for (int r = 0; r < m.length; r++) { ... m[r][c] ... }
}
for (int[] row : m) {                                   // the outer variable is a whole row
    for (int v : row) { ... }
}
```

On the 3 × 3 grid, row-major prints `1 2 3 4 5 6 7 8 9` and column-major `1 4 7 2 5 8 3 6 9`; the enhanced form gives the row sums `6 15 24`. The 1D algorithms return with a restriction to "a designated row, column, or other subsection": the maximum of column 1 fixes `c = 1` and loops over `r`; rotating row 2 right by one saves `m[2][2]`, slides the others right with `c` running *downwards*, and puts the saved value at `m[2][0]`. `m[3][0]` on three rows is out of bounds, exactly as in one dimension.

## 7. The searches and sorts, in Java

The ideas and the reasons they work are in [[Searching]] and [[Sorting]]; here are the forms, from `SearchSort.java`, all traced by printing.

- **Linear search** from either end: the first `return i` inside the loop, and `return -1` after it. On `{29, 3, 17, 8, 12}`, `linear(a, 17)` is `2` and `linear(a, 5)` is `-1`. A 2D search applies it to each row in turn.
- **Binary search**, on a *sorted* array, halving the range each call: for `41` in `{3, 8, 12, 17, 29, 41, 50}` the ranges are `[0,6] [4,6]` and the answer is `5`; for `10` they are `[0,6] [0,2] [2,2]` and then `-1`. It is written recursively here and can be written with a loop; the course asks you to trace it, not to write it.
- **Selection sort**: pass `k` finds the smallest of the unsorted part and swaps it into place `k`, so after each pass the first `k + 1` are final: `[3, 29, 17, 8, 12] [3, 8, 17, 29, 12] [3, 8, 12, 29, 17] [3, 8, 12, 17, 29]`.
- **Insertion sort**: pass `k` slides `a[k]` left through the sorted part until it fits, so after each pass the first `k + 1` are sorted but not final: `[3, 29, 17, 8, 12] [3, 17, 29, 8, 12] [3, 8, 17, 29, 12] [3, 8, 12, 17, 29]`.
- **Merge sort** splits until one element and merges sorted halves: `merged 0..1`, `merged 0..2`, `merged 3..4`, `merged 0..4`. Recursion is traced, not written, in this course; [[Recursion]] has the frames.

## Python to Java, at a glance

| Idea | Python | Java array | Java `ArrayList` |
|---|---|---|---|
| make one | `[0] * 4` | `new int[4]` | `new ArrayList<Integer>()` |
| literal | `[2, 3, 5]` | `{2, 3, 5}` | add them one by one |
| how many | `len(a)` | `a.length` | `a.size()` |
| read | `a[i]` | `a[i]` | `a.get(i)` |
| write | `a[i] = v` | `a[i] = v` | `a.set(i, v)` |
| append | `a.append(v)` | impossible | `a.add(v)` |
| insert | `a.insert(i, v)` | impossible | `a.add(i, v)` |
| delete | `del a[i]` | impossible | `a.remove(i)` |
| for each | `for v in a:` | `for (int v : a)` | `for (Integer v : a)` |
| 2D | list of lists | `int[][]` | `ArrayList<ArrayList<Integer>>` |
| element type | anything | one type, fixed | one type, an object |

## Worked examples

### Example 1: write the `ArrayList` method from its specification

> A class `Playlist` holds `private ArrayList<String> songs;`. Write `public int removeShort(int limit)`, which removes every song whose title is shorter than `limit` characters and returns how many were removed.

*Trigger: remove-while-traversing with a count. Tool: the careful `while`, advancing only after a pass that removed nothing.*

```java
public int removeShort(int limit) {
    int removed = 0;
    int i = 0;
    while (i < songs.size()) {
        if (songs.get(i).length() < limit) {
            songs.remove(i);
            removed++;
        } else {
            i++;
        }
    }
    return removed;
}
```

### Example 2: trace the list

```java
ArrayList<Integer> a = new ArrayList<Integer>();
a.add(5); a.add(2); a.add(9);
a.add(1, 7);
a.set(0, a.get(3));
a.remove(2);
```
*Trigger: a sequence of index-taking calls. Tool: rewrite the list after every line, indices included.*

`[5, 2, 9]` → `[5, 7, 2, 9]` → `a.get(3)` is `9`, so `[9, 7, 2, 9]` → remove index 2: `[9, 7, 9]`. Size 3.

### Example 3: a 2D method

> Write `public static int countAbove(int[][] grid, int t)`, the number of elements greater than `t` in the whole grid.

*Trigger: a property counted over every cell. Tool: nested loops or nested enhanced loops; the count is the running answer.*

```java
public static int countAbove(int[][] grid, int t) {
    int count = 0;
    for (int[] row : grid) {
        for (int v : row) {
            if (v > t) { count++; }
        }
    }
    return count;
}
```
For "a designated column `c`" the outer loop becomes `for (int r = 0; r < grid.length; r++)` and the test is on `grid[r][c]`.

### Example 4: which pass is this?

> After some passes, `{9, 4, 7, 1, 8}` has become `{4, 7, 9, 1, 8}`. Selection sort or insertion sort, and how many passes?

*Trigger: a snapshot of a sort. Tool: selection puts final elements at the front (the smallest so far); insertion keeps the front sorted but not final.*

The front three are sorted, but `1` is still at the back, so the front is not final: **insertion sort, after two passes** (pass 1 moves `4` in front of `9`; pass 2 moves `7` between them). Selection sort after two passes would begin `1, 4`.

## Predict, then check

1. `int[] a = new int[3]; System.out.println(a[3]);` Compile-time, run-time, or fine?
2. `String[] s = new String[2]; System.out.println(s[0].length());` What happens?
3. `for (int v : a) { v = v * 2; }` Does `a` change?
4. `ArrayList<Integer> x = ...; x.add(0, 5);` on an empty list. Legal?
5. `list.remove(1)` on `[a, b, c, d]` returns what, and leaves what?
6. `Integer p = 500, q = 500; p == q`?
7. `int[][] g = new int[4][6]; g.length + " " + g[0].length`?
8. `list.set(list.size(), "z")` on a list of size 3. Legal?

> [!success]- Answers
> 1. Run-time: `ArrayIndexOutOfBoundsException`. The compiler does not check indices.
> 2. `NullPointerException`: the slots of a `String` array start as `null`.
> 3. No. `v` is a copy.
> 4. Yes: `0 <= index <= size()`, and `size()` is 0.
> 5. Returns `b`; leaves `[a, c, d]`, with `c` now at index 1.
> 6. `false`: two objects. `p.equals(q)` is true.
> 7. `4 6`: four rows of six.
> 8. No: `set` needs an existing index, `0` to `size() - 1`. `add(list.size(), "z")` would be legal.

## Common Misconceptions (Teaching Notes)

1. **"Removing in a forward loop is fine if I use the index."** The gap closes and the next element is skipped. Walk backwards, or advance only when nothing was removed.
2. **"The enhanced-for variable *is* the element."** It is a copy of the element; assigning to it does nothing. Calling a method on it does change an object, because the copy is a reference.
3. **"`list.length`, `list[i]`."** Lists have `size()`, `get(i)` and `set(i, v)`; arrays have `length` and brackets.
4. **"Two `Integer`s compare with `==`."** They are objects. Use `equals`, or unbox.
5. **"A 2D array is a grid."** It is an array of row arrays: `m[1]` is a real array you can alias, and `m[0].length` is the column count.
6. **"An array of objects contains objects."** It contains references, `null` until set; `new Tally[3]` makes three `null`s and no tallies.
7. **"Binary search works on any array."** Only on a sorted one.

## Exam Notes

### AP Computer Science A (course effective Fall 2025)

This covers topics **4.2 to 4.13** of Unit 4 and the Java forms for **4.14 to 4.17**, whose ideas are in [[Searching]], [[Sorting]] and [[Recursion]]. Topic 4.1, ethics, is in [[Ethics and Ownership]]. Unit 4 carries 30–40 % of the exam, more than any other.

- **The written questions that are this card:** free-response Question 3, *Data Analysis with ArrayList*, and Question 4, *2D Array*: in each, "students will write one method of a given class based on provided specifications and examples", using an `ArrayList` or a 2D array. Examples 1 and 3 are those shapes. The Java Quick Reference lists the six `ArrayList` methods, `parseInt`, `parseDouble`, `split`, and the `Scanner` methods for files.
- **Often set as multiple choice:** the contents of a list after a sequence of `add`, `set` and `remove`; what a forward removal loop leaves; the value of a loop variable's assignment inside an enhanced for; row-major against column-major output; which statement throws which exception; the state of an array after $k$ passes of a named sort; the number of comparisons in a binary search.
- **Inside the course:** everything in sections 1 to 7; default values; `length` against `size()`; the enhanced for loop and its copy semantics; the standard algorithms listed in 4.5, 4.10 and 4.13, including consecutive pairs, duplicates, shift, rotate and reverse; `File`, `Scanner(File)`, `throws IOException`, `hasNext`, `next`, `nextInt`, `nextDouble`, `nextBoolean`, `nextLine`, `close`, `split`; wrapper classes and boxing; generics; `IndexOutOfBoundsException` and `ConcurrentModificationException`; `[row][col]`; tracing linear search, binary search, selection, insertion and merge sort.
- **Outside the course, by its own statements:** non-rectangular 2D arrays; keyboard input; mixing `nextLine` with other `Scanner` methods; regular-expression features of `split`; search algorithms other than linear and binary; sorts other than selection, insertion and merge; *writing* recursive code (it is traced, not written).

### Cambridge 9618 (Paper 4) and IB Computer Science

Both accept Java. 9618 Paper 4 tasks build arrays, read text files, and implement the searches and sorts in full; a Java candidate needs sections 2, 3, 6 and 7 most, and the [[Cambridge Pseudocode]] `ARRAY[1:10]` becomes `new int[10]` indexed from 0. IB's programming questions use lists and 2D arrays in the same forms.

### Where this is *not* examined

Cambridge 0478 is answered in pseudocode or Python; its arrays are in [[Arrays]].

## Connections

- **The concepts, taught in Python:** [[Arrays]] (the address formula, aliasing, 2D as a line), [[Searching]], [[Sorting]], [[Recursion]], [[File Processing and Exception Handling]].
- **Earlier companions:** [[Java Values and Expressions]], [[Java Objects, References and Strings]] (references, `Scanner`, `equals`), [[Java Control Flow]] (the loops), [[Java Classes]] (the classes whose objects are collected).
- **The structure underneath a list that grows:** [[Linked List]] (the alternative), [[Big-O Notation]] (why `add(0, x)` on a long list is slow).

## Notation Reference

| Symbol | LaTeX | Notes |
|--------|-------|-------|
| $0 \le i \le n - 1$ | `0 \le i \le n - 1` | Legal indices of an array or list of $n$ elements |
| $0 \le i \le n$ | `0 \le i \le n` | Legal positions for `add(i, obj)`; $n$ itself appends |
| $\lceil \log_2 n \rceil$ | `\lceil \log_2 n \rceil` | Upper bound on binary-search steps |
