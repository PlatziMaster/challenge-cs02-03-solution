"""Solution by <USERNAME>."""

from collections import defaultdict
from typing import List


class Solution:
    """Winner of an election."""
    
    def winner_brute_force(self, V):  # O(n^2) time, O(1) space
        """Brute force solution."""
        majority = len(V) // 2
        for v in V:
            count = 0
            for w in V:
                if w == v:
                    count += 1
            if count > majority:
                return v

    def winner_memo(self, V):  # O(n) time, O(n) space
        """Use auxiliary storage."""
        store = defaultdict(int)
        majority = len(V) // 2
        for v in V:
            store[v] += 1
        for k, v in store.items():
            if v > majority:
                return k
    
    def winner_sort(self, V):  # O(nlogn) time, O(n) space
        """Sorts the array, and find the winner."""
        #return sorted(V)[len(V)//2]
        sorted_votes = sorted(V)  # O(nlogn)
        mid = len(V) // 2
        return sorted_votes[mid]

    def winner_count(self, V, winner, start, end):  # O(n)
        count = 0
        for i in range(start, end+1):
            count += 1 if V[i] == winner else 0
        return count

    def winner_recursive(self, V, start, end):
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
