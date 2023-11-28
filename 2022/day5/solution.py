import textwrap
from itertools import dropwhile
import re
from math import ceil

def make_stacks(lines: list[str]) -> list[list[str]]:
    ln = len(lines[0])
    width = 4 # each box takes three characters and after that comes one space
    amount_stacks = ceil(ln / width)
    stacks = [[] for _ in range(amount_stacks)]
    for l in lines:
        if l == '\n':
            break
        wrap = textwrap.wrap(l, width, drop_whitespace=False)
        for (i,w) in enumerate(wrap):
            if w[0] == '[':
                stacks[i].append(w[1])
    return stacks

def execute_instructions(instructions: list[str], stacks: list[list[str]], move_many) -> list[list[str]]:
    stacks = stacks.copy()
    for ins in instructions:
        parts = re.search('move ([0-9]+) from ([0-9]+) to ([0-9]+)', ins)
        amount = int(parts.group(1))
        f = int(parts.group(2)) - 1
        t = int(parts.group(3)) - 1
        if move_many:
            stacks[t] = stacks[f][0:amount] + stacks[t]
            stacks[f] = stacks[f][amount:]
        else:
            for _ in range(amount):
                stacks[t].insert(0, stacks[f].pop(0))
    return stacks
    
if __name__ == "__main__":
    from sys import stdin
    lines = list(map(lambda x: x[:-1], stdin.readlines()))
    instructions = list(dropwhile(lambda x: x and x[0] != 'm', lines))[1:]
    # part 1
    stacks = execute_instructions(instructions, make_stacks(lines), False)
    print(''.join([x[0] for x in stacks]))
    # part 2
    stacks = execute_instructions(instructions, make_stacks(lines), True)
    print(''.join([x[0] for x in stacks]))