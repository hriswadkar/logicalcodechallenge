# Getting comfortable in Python (for C# / Java developers)

You already know how to program. You are not learning *programming* — you are
learning to **translate ideas you already own** into Python. Treat every Python
feature as "what's the C#/Java equivalent?" and the discomfort disappears fast.

## 1. The mental shift

| What feels weird | Why it's actually fine |
|------------------|------------------------|
| No `{ }` braces | **Indentation** defines blocks. 4 spaces = one level. The colon `:` opens a block. |
| No `;` | Line end = statement end. |
| No type declarations | Types still exist and matter; you just don't *write* them. Add optional hints (`x: int`) for clarity. |
| `self` everywhere | Same as C#/Java `this`, but Python makes it explicit as the first method parameter. |
| "English-like" reads odd | It's just terser. `if x in seen:` == `if (seen.ContainsKey(x))`. |

## 2. C# / Java → Python cheat sheet

| Concept | C# / Java | Python |
|---------|-----------|--------|
| Variable | `int x = 5;` | `x = 5` |
| Constant-ish | `const int N = 10;` | `N = 10` (convention: UPPER_CASE) |
| List / array | `List<int> a = new();` | `a = []` |
| Add to list | `a.Add(3);` | `a.append(3)` |
| Length | `a.Count` / `a.length` | `len(a)` |
| Dictionary / map | `Dictionary<int,int> d = new();` | `d = {}` |
| Put in map | `d[k] = v;` | `d[k] = v` |
| Contains key | `d.ContainsKey(k)` | `k in d` |
| Set | `HashSet<int> s = new();` | `s = set()` |
| For-i loop | `for (int i=0;i<n;i++)` | `for i in range(n):` |
| For-each | `foreach (var x in a)` | `for x in a:` |
| For-each with index | `for (int i...) a[i]` | `for i, x in enumerate(a):` |
| While | `while (cond) { }` | `while cond:` |
| If / else if / else | `if/else if/else` | `if / elif / else:` |
| Method | `int F(int x) {...}` | `def f(x):` |
| Null | `null` | `None` |
| Boolean | `true` / `false` | `True` / `False` |
| String interpolation | `$"x={x}"` | `f"x={x}"` |
| Ternary | `c ? a : b` | `a if c else b` |
| And / Or / Not | `&&` `||` `!` | `and` `or` `not` |

## 3. Python idioms worth learning early (these make code "click")

```python
# enumerate: index + value together (instead of range(len(...)) + a[i])
for i, value in enumerate(nums):
    ...

# dict.get with default (no KeyError)
count = counts.get(key, 0)

# comprehensions: build a list/dict in one line
squares = [x * x for x in nums]
evens   = [x for x in nums if x % 2 == 0]

# unpacking / swap (no temp variable)
a, b = b, a

# slicing
first_three = nums[:3]
last_two    = nums[-2:]
reversed_   = nums[::-1]

# truthiness: empty list/dict/string/0/None are all "falsy"
if not nums:      # "if the list is empty"
    return []

# useful standard library for these challenges
from collections import defaultdict, Counter, deque
import heapq       # priority queue / heap
import math        # gcd, sqrt, etc. (great for Project Euler)
```

## 4. How to actually get comfortable (the routine)

1. **Keep solving these challenges in Python**, one *pattern* at a time. Repetition
   in a real context beats tutorials.
2. For each problem, **first write it in the way you'd do in C#**, then rewrite it
   the idiomatic Python way (e.g. swap `range(len(x))` for `enumerate`). Seeing both
   trains your eye.
3. **Type it yourself** in VS Code — muscle memory matters. Let Pylance (VS Code's
   Python helper) autocomplete and show you methods.
4. Keep this cheat sheet open. After ~2 weeks it'll be in your head.
5. Optional short read when you have downtime: the official
   [Python Tutorial](https://docs.python.org/3/tutorial/) sections 3–5 (numbers,
   lists, dicts, control flow). Skim, don't grind.

## 5. VS Code tips for Python

- Install the **Python** and **Pylance** extensions (Microsoft). Pylance gives
  IntelliSense/autocomplete just like Visual Studio does for C#.
- Run the current file: the ▶ "Run Python File" button, or `python file.py` in the
  terminal.
- Red squiggles = syntax/type issues; hover to read them — they teach you fast.
