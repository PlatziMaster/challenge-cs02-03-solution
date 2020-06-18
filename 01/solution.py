"""Solution by <USERNAME>."""

from typing import List


class Solution:
    """Combining the conquered!"""

    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None: # pylint: disable=C0103
        """Solution to problem."""
        while m > 0 and n > 0:
            if A[m-1] >= B[n-1]:
                A[m+n-1] = A[m-1]
                m -= 1
            else:
                A[m+n-1] = B[n-1]
                n -= 1
        if n > 0:
            A[:n] = B[:n]
