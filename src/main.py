from aocd import get_data
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
print(elves.top_x(1))