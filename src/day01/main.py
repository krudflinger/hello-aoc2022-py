from aocd import get_data


def part_a(data: str) -> int:
    groups = data.strip().split("\n\n")
    sums = [sum([int(calorie) for calorie in group.split("\n")])
            for group in groups]
    return max(sums)


def part_b(data: str) -> int:
    groups = data.strip().split("\n\n")
    sums = [sum([int(calorie) for calorie in group.split("\n")])
            for group in groups]
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
