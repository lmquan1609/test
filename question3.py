# Minimum Adjacent Swaps to Reach the Kth Smallest Number

# Time Complexity:
#       O(KN) where N is number of string `num` and K is k-th smallest number

# Space Complexity:
#       O(N)

from typing import List
from bisect import bisect_right

def get_min_swaps(num: str, k: int) -> int:
    """Determine the minimum adjacent swaps to reach the next Kth smallest number

    Args:
        num (str): Given number in str
        k (int): Given k

    Returns:
        int: Minimum swaps
    """
    nums_len = len(num)
    nums = list(map(int, num))

    def next_greater_number(nums: List[int]) -> List[int]:
        """First thing to do is to find out the next greater number given array of integer

        Args:
            nums (List[int]): Given array of integer

        Returns:
            List[int]: Array of integer which is the next greater number if given array of integer
        """
        # Construct the mono-increasing stack
        stack = []
        for i in range(nums_len - 1, -1, -1):
            # constructing the stack until we reach the value which is not in
            # increasing order of stack if the value is added to stack
            if stack and nums[i] < stack[-1]:
                break
            stack.append(nums[i])
        
        if len(stack) == nums_len:
            return -1
        
        # Swap the value at index i where we break the loop, with the 
        # larger value in stack such that the difference between them is smallest
        swap_idx = bisect_right(stack, nums[i])
        nums[i], stack[swap_idx] = stack[swap_idx], nums[i]
        return nums[:i + 1] + stack

    def count_steps(origin: List[int], target: List[int]) -> int:
        """Count number of swap to transform from origin to target

        Args:
            origin (List[int]): Original list of integer
            target (List[int]): Target list of integer we want to transform

        Returns:
            int: Number to step to transform from original to target list of integer
        """
        steps = 0
        for lhs in range(nums_len):
            # 2 pointer technique where left hand side pointer point to the pivotal value
            # and right hand side pointers slide the array to find the same value with pivot
            rhs = lhs
            while rhs < nums_len and origin[lhs] != target[rhs]:
                rhs += 1
            
            # After finding the value same with pivot, swap the value with its adjacent until
            # the index of left hand side matches with that of right hand side
            while lhs < rhs:
                target[rhs], target[rhs - 1] = target[rhs - 1], target[rhs]
                rhs -= 1
                steps += 1
        
        return steps
    
    # Find out the Kth larger number
    larger_nums = nums[:]
    for _ in range(k):
        larger_nums = next_greater_number(larger_nums)
    
    # Get number of swaps
    return count_steps(nums, larger_nums)