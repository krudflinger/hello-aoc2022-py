from aocd import get_data
from ..utils.aoctimer import aoctimer


test_data ='''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''
data = get_data(day=4,year=2022)


def is_overlapping(l1,l2,r1,r2):
    return max(l1,r1) <= min(r2,l2)

totals=[]
sections = [([int(v) for v in pair[0].split('-')],[int(v) for v in pair[1].split('-')]) for pair in [sections.split(',') for sections in data.splitlines()]]


@aoctimer
def answer_1():
    count=0
    for section in sections:
        left,right=range(section[0][0],section[0][1]+1), range(section[1][0],section[1][1]+1)
        if left.start in right and left[-1] in right:
            count+=1
        elif right.start in left and right[-1] in left:
            count+=1
    print(count)

@aoctimer
def answer_2():
    count=0
    for section in sections:
        if is_overlapping(section[0][0],section[0][1],section[1][0],section[1][1]):
            count+=1
    print(count)

if __name__ =='__main__':
    answer_1()
    answer_2()