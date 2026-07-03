"""
Problem: Two Sum — https://leetcode.com/problems/two-sum/
Pattern: Arrays & Hashing

Approach (fill in as you work through the framework):
  1. Restate:
  2. Example trace:
  3. Brute force + complexity:
  4. Bottleneck:
  5. Optimized idea + complexity:
"""

from typing import List


class Solution:
    
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        pass
    
    def two_sum_optimized(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            partner = target - nums[i]
            if partner in seen:
                return [seen[partner], i]
            seen[nums[i]] = i



if __name__ == "__main__":
    sol = Solution()
    # Try these once you've written your solution:
    print(sol.two_sum_optimized([2, 7, 11, 15], 9))   # expected [0, 1]
    print(sol.two_sum_optimized([3, 2, 4], 6))        # expected [1, 2]
    print(sol.two_sum_optimized([3, 3], 6))           # expected [0, 1]
