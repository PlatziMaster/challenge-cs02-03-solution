"""Assignment grader."""

from copy import copy
import sys

from solution import Solution


def read_test_case():
    """Read test case from STDIN and return parsed list."""
    raw_input = input()
    parsed_input = [int(x) for x in raw_input.split(',')] if raw_input else []
    raw_want = input()
    parsed_want = [int(x) for x in raw_want.split(',')] if raw_want else []
    return parsed_input, parsed_want


if __name__ == '__main__':
    test_case, want = read_test_case()
    sol = Solution()
    original_input = copy(test_case)
    output = sol.sigma_transformation(test_case)  # pylint: disable=E1101
    if output != want:
        print("\t❌ Test case failed:")
        print("\t\tInput:", original_input)
        print("\t\tGot:", output)
        print("\t\tWant:", want)
        sys.exit(1)
    print("\t✅ Test case accepted")
