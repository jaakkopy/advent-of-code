from functools import cache

lines = []

@cache
def ways(i, j, k, l):
    li = lines[l]    
    if i == len(li[0]):
        if j == len(li[1]) and k == 0:
            return 1
        if j == len(li[1]) - 1 and k == li[1][j]:
            return 1
        return 0
    dot = 0
    tag = 0
    if li[0][i] == '.' or li[0][i] == '?':
        # either all the sequences of '#'s have been handled or the next has not yet started
        if k == 0:
            dot = ways(i+1, j, 0, l)
        # this sequence of '#'s is done, move to the next one
        elif j < len(li[1]) and li[1][j] == k:
            dot = ways(i+1, j+1, 0, l)
    # place a '#' here and increment k by 1
    if li[0][i] == '#' or li[0][i] == '?':
        tag = ways(i+1, j, k+1, l)
    return dot + tag


if __name__ == "__main__":
    from sys import stdin
    lines = [[y[0], [int(z) for z in y[1].split(",")]] for y in [x.rstrip().split() for x in stdin.readlines()]]
    print(sum(ways(0,0,0,i) for i in range(len(lines)))) # part 1

    multiplied = []
    for [syms, nums] in lines:
        multiplied.append((('?'.join(syms for _ in range(5))), nums * 5))

    lines = multiplied
    ways.cache_clear()
    print(sum(ways(0,0,0,i) for i in range(len(lines)))) # part 2