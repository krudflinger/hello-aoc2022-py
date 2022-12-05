from aocd import get_data
from ..utils.aoctimer import aoctimer

from dataclasses import dataclass
from typing import List



@dataclass
class Elf:
    id: int
    inventory: List[int]

    def total(self):
        return sum(self.inventory)

@dataclass
class Elves:
    cohort: List[Elf]

    def top_x(self, rank):
        sort=sorted(self.cohort, key = lambda x: x.total())
        return sort[-rank:] 

inventory = []
iter = 0
cohort = []
for elf in get_data().split("\n\n"):
    iter+=1 
    cohort.append(Elf(id=iter,inventory=[int(i) for i in elf.splitlines()]))
elves=Elves(cohort=cohort)

answer_1 = sum([elf.total() for elf in elves.top_x(1)])
answer_2 = sum([elf.total() for elf in elves.top_x(3)])

if __name__ == '__main__': 
    print(f'The answer to question 1 is {answer_1}')
    print(f'The answer to question 2 is {answer_2}')