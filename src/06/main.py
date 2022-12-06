from aocd import get_data
from ..utils.aoctimer import aoctimer


test_data = """mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
"""

data = list(get_data(day=6, year=2022))


@aoctimer
def seek_message(data, seek) -> int:
    count = 0
    for b in data:
        count += 1
        unique = set(data[count - seek : count])
        if len(unique) == seek:
            return count


def answer_1():
    print(seek_message(data, 4))


def answer_2():
    print(seek_message(data, 14))


if __name__ == "__main__":
    answer_1()
    answer_2()
