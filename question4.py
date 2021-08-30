# Minimum Interval to Include Each Query

# Time Complexity
# O(NlogN + QlogQ + (N + Q)logQ) where N in length of `intervals` and Q is length of queries
#     - First O(NlogN) is used for sorting `intervals`
#     - Next O(QlogQ) is used for sorting `queries`
#     - Last O((N + Q)logQ): 
#         - First O(N + Q) is used to call DSU in (N + Q) times
#         - Second O(logQ) for each `find` in DSU

# Space Complexity:
#  O(Q)
# Initialize the Union Find class

from typing import List
from bisect import bisect_left, bisect_right

class DSU:
    def __init__(self, length):
        self.parents = list(range(length))
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

def min_interval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    """Get the minimum interval for each query

    Args:
        intervals (List[List[int]]): Given intervals
        queries (List[int]): Given queries

    Returns:
        List[int]: Minimum interval for each query
    """    
    queries_len = len(queries)
    # Initialize result_dsu which is length of size for each DSU index
    result_dsu = [-1] * queries_len

    # Firstly sort the query by its value of query
    queries = sorted((query, idx) for idx, query in enumerate(queries))
    # Then sort the intervals by its gap
    intervals.sort(key=lambda interval: interval[1] - interval[0])

    # Initialize the DSU object
    dsu = DSU(queries_len + 1)

    # Loop over the intervals from the interval which have smallest to largest gap
    for start, end in intervals:
        # Find out the left and right index of `start` and `end` in sorted `queries`
        lhs = bisect_left(queries, (start, -1))
        rhs = bisect_right(queries, (end, queries_len))

        # after determining which query should be assigned to the interval
        # we assign the query to the intervals such that for next intervals,
        # we can skip these queries
        lhs_dsu = dsu.find(lhs)
        while lhs_dsu < rhs:
            result_dsu[lhs_dsu] = end - start + 1
            dsu.parents[lhs_dsu] = lhs_dsu + 1
            lhs_dsu = dsu.find(lhs_dsu)
    
    # Initialize the result array to return
    result = [-1] * queries_len
    # Assign the minimum length we determined from `result_dsu` to map with
    # final `result`
    for idx, (_, orig_idx) in enumerate(queries):
        result[orig_idx] = result_dsu[idx]
    return result