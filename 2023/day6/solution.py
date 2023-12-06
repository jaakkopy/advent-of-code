from math import sqrt, ceil
from operator import mul
from functools import reduce

def dist_traveled(T, t):
    return t*(T-t)

def winning_range(T, d):
    a = sqrt(T**2 - 4*d)/2
    l = ceil(T/2 - a)
    r = ceil(T/2 + a)
    if dist_traveled(T, l) == d:
        l += 1
    if dist_traveled(T, r) <= d:
        r -= 1
    return (l, r)

def amount_solutions(T, d):
    (l, r) = winning_range(T, d)
    return r - l + 1

if __name__ == "__main__":
    from sys import stdin
    lines = stdin.readlines()
    games = list(zip(
        [int(x) for x in lines[0].split("Time:")[1].split()], 
        [int(x) for x in lines[1].split("Distance:")[1].split()]
    ))
    solutions = map(lambda g: amount_solutions(g[0], g[1]), games)
    part1 = reduce(mul, solutions, 1)
    print(part1)