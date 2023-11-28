from math import log2
from functools import reduce

def char_num(c):
    o = ord(c)
    if o < 97:
        return o - 39 
    return o - 97

def priority(bitsequence):
    return int(log2(bitsequence)) + 1

'''
- let a,..z,A,...,Z correspond to 0,...,25,26,...,51
- use bitwise or to set left and right side, and bitwise and to find the common one
- find the priority, i.e the position of the letter, with log2 + 1
'''
def counts(lines):
    priority_sum = 0
    for x in lines:
        l = 0
        r = 0
        mid = len(x) // 2
        for i in range(0, mid):
            l |= (1 << char_num(x[i]))
            r |= (1 << char_num(x[i + mid]))
        priority_sum += priority(l & r)
    return priority_sum 

def row_counts(lines, checkcount):
    priority_sum = 0
    ln = len(lines)
    for i in range(0, ln, checkcount):
        sacks = []
        for j in range(checkcount):
            s = 0
            for c in lines[i + j]: 
                s |= (1 << char_num(c))
            sacks.append(s)
        all_sacks = reduce(lambda x,y: x & y, sacks)
        priority_sum += priority(all_sacks)
    return priority_sum

if __name__ == "__main__":
    from sys import stdin
    lines = list(map(lambda x: x.rstrip(), stdin.readlines()))
    # part 1
    cs = counts(lines)
    print(cs)
    # part 2:
    cs = row_counts(lines, 3)
    print(cs)