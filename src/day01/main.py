from aocd import get_data
import itertools


def part_a(data):
    manifest = [int(calorie) if calorie else calorie
                for calorie in data.splitlines()]
    sums = [sum(group)
            for key, group in itertools.groupby(manifest, lambda x: x == '')
            if not key]
    return max(sums)


def part_b(data):
    manifest = [int(calorie) if calorie else calorie
                for calorie in data.splitlines()]
    sums = [sum(group)
            for key, group in itertools.groupby(manifest, lambda x: x == '')
            if not key]
    return sum(sorted(sums, reverse=True)[:3])


test_data = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

if __name__ == "__main__":
    assert part_a(test_data) == 24000
    assert part_b(test_data) == 45000

    data = get_data(day=1, year=2022)
    print(part_a(data))
    print(part_b(data))
