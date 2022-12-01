from aocd import get_data
from ..utils.aoctimer import aoctimer


@aoctimer
def part_a(data):
    # your code here..
    return result  # noqa: F821


@aoctimer
def part_b(data):
    # more code here..
    return result  # noqa: F821


test_data = """\
some example test data
"""

if __name__ == "__main__":
    assert part_a(test_data) == "expected test result a"
    assert part_b(test_data) == "expected test result b"

    data = get_data(day=1, year=2022)
    print(part_a(data))
    print(part_b(data))
