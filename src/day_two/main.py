from aocd import get_data
from ..utils.aoctimer import aoctimer



rules = {2: {1:0,0:2,2:1}, 0: {0:1,2:0,1:2}, 1:{0:0,1:1,2:2}}
def char_position(letter):
    return ord(letter.lower()) - 97


test_data = """A Y
B X
C Z
"""
import functools

@functools.cache
def rps(opponent, player=None, outcome=None):
    opponent = char_position(opponent)
    if player is None:
        outcome = abs(char_position(outcome))-23
        player = [k for k,v in rules[outcome].items() if opponent==v][0]
    elif outcome is None: 
        player = abs(char_position(player))-23
        outcome=[k for k,v in rules.items() if v[player]==opponent][0]
    return ((outcome*2)+outcome)+player+1

@aoctimer
def answer_1():
    data = get_data(day=2,year=2022)
    games= [game.split() for game in data.splitlines()]

    results=[]
    for game in games:
        results.append(rps(opponent=game[0],player=game[1]))
    print(sum(results))

@aoctimer
def answer_2():
    data = get_data(day=2,year=2022)
    games= [game.split() for game in data.splitlines()]

    results=[]
    for game in games:
        results.append(rps(opponent=game[0],outcome=game[1]))
    print(sum(results))
if __name__=='__main__':
    answer_1()
    answer_2()
