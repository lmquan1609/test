# Splitting a String Into Descending Consecutive Values

# Time Complexity:
#     O(N^2) where N is length of string

# Space Complexity:
#     O(N) to store the implicit stack for recursion and to save the `candidates`

def split_string(s : str) -> bool:
    """Check whether we can constructs the array of integer where the previous 
        value in the array need to be larger than current one by 1

    Args:
        s (str): given integer string

    Returns:
        bool: True if we can construct; otherwise False
    
    Time Complexity:
        O(N^2) where N is length of string
    
    Space Complexity:
        O(N) to store the implicit stack for recursion and to save the `candidates`
    """    
    str_len = len(s)

    # initialize the array containing integer which difference between 2 
    # consecutive values is 1
    candidates = []

    def dfs(start : int) -> bool:
        """Backtrack the possible integer by splitting `s`

        Args:
            start (int): index in `s` such that from the index, we find out
                the integer which decreases by 1 from last value in `candidates`

        Returns:
            bool: whether from the `start` index we can construct the valid `candidates`
        """        
        if start == str_len:
            return len(candidates) > 1

        # Take the `start` as the left hand side pointer, we slide the right hand
        # side pointer to check whether we have the value from the `start` index which
        # decreases by 1 from last value in `candidates`
        lhs = start
        if len(candidates) > 0:
            target = candidates[-1]
            for rhs in range(start + 1, str_len + 1):
                if target - int(s[lhs:rhs]) == 1:
                    # if we have any valid integer, add the candidate
                    candidates.append(int(s[lhs:rhs]))
                    # Go to next index
                    if dfs(rhs):
                        return True
                    # otherwise pop out the integer
                    candidates.pop()
        else:
            # when our `candidates` does not have any integers, 
            # we append new integer to candidate rather than to declare `target`
            for rhs in range(start + 1, str_len + 1):
                candidates.append(int(s[lhs:rhs]))
                if dfs(rhs):
                    return True
                candidates.pop()
        return False

    # Start backtracking from 0 index
    return dfs(0)

print(split_string('1234'))