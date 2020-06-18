"""Solution by <USERNAME>."""

from collections import defaultdict
from typing import List


class Solution:
    """Winner of an election."""

    def winner_brute_force(self, V):  # pylint: disable=C0103
        """Brute force solution.

        Analysis:
            - Time: O(n^2)
            - Space: O(1)
        """
        majority = len(V) // 2
        for vote in V:
            count = 0
            for vote_2 in V:
                if vote_2 == vote:
                    count += 1
            if count > majority:
                return vote
        return None

    def winner_memo(self, V):  # pylint: disable=C0103
        """Use auxiliary storage.

        Analysis:
            - Time: O(n)
            - Space: O(n)
        """
        store = defaultdict(int)
        majority = len(V) // 2
        for vote in V:
            store[vote] += 1
        for k, vote in store.items():
            if vote > majority:
                return k
        return None

    def winner_sort(self, V):  # pylint: disable=C0103
        """Sorts the array, and find the winner.

        Analysis:
            - Time: O(nlogn) time
            - Space: O(n) if new array is created, O(1) if sorted in place.
        """
        sorted_votes = sorted(V)
        mid = len(V) // 2
        return sorted_votes[mid]

    def winner_count(self, V, winner, start, end):  # pylint: disable=C0103
        """Return the number of occurrences of winner in V[start:end+1].

        Analysis:
            - Time: O(n)
            - Space: O(1)
        """
        count = 0
        for i in range(start, end+1):
            count += 1 if V[i] == winner else 0
        return count

    def winner_recursive(self, V, start, end):  # pylint: disable=C0103
        """Solves the problem using a divide and conquer strategy.

        Analysis:
            - Time: O(nlogn)
            - Space: O(logn)
        """
        if start == end:
            return V[start]

        mid = int((end-start)/2 + start)

        winner_left = self.winner_recursive(V, start, mid)
        winner_right = self.winner_recursive(V, mid+1, end)

        if winner_left == winner_right:
            return winner_left

        left_count = self.winner_count(V, winner_left, start, mid)
        right_count = self.winner_count(V, winner_right, mid+1, end)

        return winner_left if left_count > right_count else winner_right

    def winner(self, V: List[int]) -> int: # pylint: disable=C0103
        """Solution to problem."""
        return self.winner_recursive(V, 0, len(V)-1)
