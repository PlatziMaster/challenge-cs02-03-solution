"""Solution by <USERNAME>."""

from typing import List


class Solution:
    """Sigma transformation."""

    def sigma_transformation(self, A: List[int]) -> List[int]: # pylint: disable=C0103
        """Solution to problem."""
        for i in range(1, len(A)):
            # A[i] += A[i-1]
            A[i] = A[i] + A[i-1]
        return A
