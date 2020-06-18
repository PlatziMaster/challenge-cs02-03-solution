"""Assignment grader."""

from copy import copy
import sys

from solution import Solution


def read_test_case():
    """Read test case from STDIN and return parsed list."""
    raw_a = input()
    parsed_a = [int(x) for x in raw_a.split(',')] if raw_a else []
    parsed_m = int(input())

    raw_b = input()
    parsed_b = [int(x) for x in raw_b.split(',')] if raw_b else []
    parsed_n = int(input())

    raw_want = input()
    parsed_want = [int(x) for x in raw_want.split(',')] if raw_want else []
    return parsed_a, parsed_m, parsed_b, parsed_n, parsed_want


if __name__ == '__main__':
    A, m, B, n, want = read_test_case()
    sol = Solution()
    original_input = copy(A)
    sol.merge(A, m, B, n)
    if A != want:
        print("\t❌ Test case failed:")
        print("\t\tInput:", original_input)
        print("\t\tGot:", A)
        print("\t\tWant:", want)
        sys.exit(1)
    print("\t✅ Test case accepted")
