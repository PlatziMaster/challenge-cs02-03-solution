"""Assignment grader."""

import sys

from solution import Solution


def read_test_case():
    """Read test case from STDIN and return parsed list."""
    return [int(x) for x in input().split(',')], int(input())


if __name__ == '__main__':
    test_case, want = read_test_case()
    sol = Solution()
    output = sol.winner(test_case)  # pylint: disable=E1101
    if output != want:
        print("\t❌ Test case failed:")
        print("\t\tInput:", test_case)
        print("\t\tGot:", output)
        print("\t\tWant:", want)
        sys.exit(1)
    print("\t✅ Test case accepted")
