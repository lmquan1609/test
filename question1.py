# Minimum Distance to the Target Element

# Time Complexity
#     O(N) where N is the length of `nums`

# Space Complexity:
#     O(1)

from typing import List

def min_distance_from_target(nums: List[int], target: int, start: int) -> int:
    """Get minimum distance from `start` such that the value at given value is equal to `target`

    Args:
        nums (List[int]): given array where length <= 1000
        target (int): target to search
        start (int): given start

    Returns:
        int: Minimum distance
    """
    # Initialize the `dist` which is minimum distance we want to get
    dist = 0
    nums_len = len(nums)

    # Increase the `dist` until we get the target
    while start + dist < nums_len or start - dist >= 0:
        if start + dist < nums_len and start - dist >= 0:
            if nums[start + dist] == target or nums[start - dist] == target:
                return dist
        elif start + dist < nums_len:
            if nums[start + dist] == target:
                return dist
        else:
            if nums[start - dist] == target:
                return dist
        dist += 1