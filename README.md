# logicalcodechallenge

A personal workspace for solving logical code challenges (LeetCode, Project Euler)
and, most importantly, for building **problem-solving logic** — not memorizing answers.

Languages: Python (primary, for practice), with Java and C# as fallbacks.

## How this repo is organized

Solutions are grouped by **pattern**, because recognizing the pattern is 80% of
solving a problem:

```
arrays_and_hashing/
two_pointers/
sliding_window/
stack/
binary_search/
linked_list/
trees/
heap/
backtracking/
graphs/
dynamic_programming/
math/            <- Project Euler lives here too
```

Each problem gets its own folder containing:

- `problem.md` — the problem statement and the framework prompts to work through
- `solution.py` — your solution (start from `TEMPLATE/solution_template.py`)

## The 5-step problem-solving framework

Apply this to **every** problem. See [FRAMEWORK.md](FRAMEWORK.md) for the full guide.

1. **Restate** the problem in your own words; write down inputs and outputs.
2. **Hand-trace** at least one example on paper before coding.
3. **Brute force first** — get *a* working idea, and state its time/space cost.
4. **Find the bottleneck** — what is the slow/repeated step?
5. **Optimize** — pick a data structure or technique that removes the bottleneck;
   state the new time/space cost.

## Progress log

| # | Problem | Pattern | Language | Status |
|---|---------|---------|----------|--------|
| 1 | [Two Sum](arrays_and_hashing/two_sum/problem.md) | Arrays & Hashing | Python | In progress |
