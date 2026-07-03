# 1. Two Sum

**Difficulty:** Easy
**Pattern:** Arrays & Hashing
**Link:** https://leetcode.com/problems/two-sum/

## Statement

Given an array of integers `nums` and an integer `target`, return the **indices**
of the two numbers such that they add up to `target`.

- Exactly one valid answer exists.
- You may not use the same element twice.
- You can return the answer in any order.

### Examples

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]          # nums[0] + nums[1] = 2 + 7 = 9

Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]          # nums[1] + nums[2] = 2 + 4 = 6

Input:  nums = [3, 3], target = 6
Output: [0, 1]
```

## Work through the framework (write your answers here)

1. **Restate:** inputs? outputs?
2. **Hand-trace:** for `[3, 2, 4], target = 6`, which indices, and why?
3. **Brute force:** most obvious approach? its time complexity?
4. **Bottleneck:** for each number you look for `target - num`. What makes
   "have I already seen `target - num`?" instant?
5. **Optimize:** new approach + its time/space complexity.

Then write your code in `solution.py`.
