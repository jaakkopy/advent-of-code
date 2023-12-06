from math import sqrt, ceil
from operator import mul
from functools import reduce

def dist_traveled(T, t):
    return t*(T-t)

'''
let T equal the time limit of the game and d the distance limit. The distance traveled is t(T-t) = -t^2 + tT where t is the time spent pressing the button.
Solve for t:
Tt - t^2 > d
t^2 - Tt + d < 0

-> (T - sqrt(T^2 - 4d))/2 < t < (T + sqrt(T^2 - 4d))/2

also take ceil and check edges of the interval
'''
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
    times = [x for x in lines[0].split("Time:")[1].split()]
    dists = [x for x in lines[1].split("Distance:")[1].split()]
    solutions = map(lambda g: amount_solutions(g[0], g[1]), zip(map(int, times), map(int, dists)))
    
    part1 = reduce(mul, solutions, 1)
    print(part1)

    part2_game = (int(''.join(times)), int(''.join(dists)))
    print(amount_solutions(part2_game[0], part2_game[1]))