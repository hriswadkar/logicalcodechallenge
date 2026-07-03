import time


def two_sum_nested(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_fast(nums, target):
    seen = {}
    for i in range(len(nums)):
        partner = target - nums[i]
        if partner in seen:
            return [seen[partner], i]
        seen[nums[i]] = i


for n in [1000, 4000, 8000]:
    nums = list(range(n))
    target = 2 * n - 3          # forces the answer to be the last two elements

    start = time.perf_counter()
    two_sum_nested(nums, target)
    t_nested = time.perf_counter() - start

    start = time.perf_counter()
    two_sum_fast(nums, target)
    t_fast = time.perf_counter() - start

    print(f"n={n:>5}  nested={t_nested*1000:9.2f} ms   fast={t_fast*1000:7.3f} ms   "
          f"nested is {t_nested/t_fast:6.0f}x slower")
