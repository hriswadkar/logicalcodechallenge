"""Tests for the Two Sum solutions.

Loaded by pytest (run `pytest` from the repo root). Solutions live in their
problem folders, so we load the file by path to avoid module-name clashes as
more problems (each with their own solution.py) are added.
"""

import importlib.util
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SOLUTION_PATH = REPO_ROOT / "arrays_and_hashing" / "two_sum" / "solution.py"


def _load(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


Solution = _load(SOLUTION_PATH).Solution

# (nums, target, expected pair of indices as a sorted tuple)
CASES = [
    ([2, 7, 11, 15], 9, (0, 1)),
    ([3, 2, 4], 6, (1, 2)),
    ([3, 3], 6, (0, 1)),
    ([-3, 4, 3, 90], 0, (0, 2)),   # negatives still work
]


@pytest.mark.parametrize("nums, target, expected", CASES)
def test_two_sum_bruteforce(nums, target, expected):
    result = Solution().two_sum(nums, target)
    assert tuple(sorted(result)) == expected


@pytest.mark.parametrize("nums, target, expected", CASES)
def test_two_sum_optimized(nums, target, expected):
    result = Solution().two_sum_optimized(nums, target)
    assert tuple(sorted(result)) == expected
