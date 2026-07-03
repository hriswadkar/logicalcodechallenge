# The Problem-Solving Framework

The goal is not to solve *this* problem — it's to build a repeatable process so you
can solve problems you've never seen. Follow these steps every single time.

## Step 1 — Restate the problem

- Rewrite the problem in your own words.
- Write down exactly what the **inputs** are (types, ranges, can they be empty?
  negative? duplicates?) and what the **output** should be.
- Note constraints — they hint at the expected complexity. (e.g. n up to 10^5
  usually means O(n) or O(n log n) is expected, not O(n^2).)

## Step 2 — Hand-trace an example

- Take a small concrete example and solve it **by hand**, writing each step.
- Make up an edge case too (empty input, one element, all duplicates, negatives).
- If you can't solve it by hand, you can't code it. This step alone prevents most
  "I don't know where to start" moments.

## Step 3 — Brute force first

- Write the most obvious solution, even if it's slow. A working slow answer beats
  a broken clever one.
- State its **time and space complexity** in Big-O.
- This gives you a correct baseline to compare against.

## Step 4 — Find the bottleneck

- Look at the brute force: what work is **repeated** or **wasted**?
- Common bottlenecks and their fixes:
  | Bottleneck | Often fixed by |
  |------------|----------------|
  | Searching a list repeatedly | hash set / hash map (O(1) lookup) |
  | Re-computing sums of ranges | prefix sums |
  | Nested loops over sorted data | two pointers |
  | Re-solving overlapping subproblems | memoization / DP |
  | Finding min/max repeatedly | heap |

## Step 5 — Optimize and verify

- Apply the technique, then re-check correctness against your Step 2 examples.
- State the new time/space complexity and confirm it meets the constraints.
- Only now, clean up the code.

## The core patterns (learn to recognize these)

1. **Arrays & Hashing** — "have I seen this value?" → set/dict
2. **Two Pointers** — sorted array, pair/triplet sums, palindromes
3. **Sliding Window** — longest/shortest contiguous subarray meeting a condition
4. **Stack** — matching brackets, "next greater element", undo-style logic
5. **Binary Search** — sorted data, or "search on the answer"
6. **Linked List** — pointer manipulation, fast/slow pointers
7. **Trees** — DFS/BFS traversal, recursion
8. **Heap / Priority Queue** — top-k, streaming min/max
9. **Backtracking** — generate all combinations/permutations/subsets
10. **Graphs** — BFS/DFS, connected components, shortest path
11. **Dynamic Programming** — overlapping subproblems, optimal substructure
12. **Math / Number theory** — Project Euler territory (primes, gcd, modular math)
