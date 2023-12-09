from math import lcm

def part1(path, instructions, start, end_condition):
    l = len(instructions)
    c = 0
    n = start
    while not end_condition(n):
        i = 0 if instructions[c % l] == 'L' else 1
        n = path[n][i]
        c += 1
    return c

def part2(path, instructions):
    return lcm(*[part1(path, instructions, n, lambda x: x[2] == 'Z') for n in list(filter(lambda x: x[2] == 'A', path))])


if __name__ == "__main__":
    from sys import stdin
    lines = [x.rstrip() for x in stdin.readlines()]
    instructions = lines[0]
    path = {}
    for i in lines[2:]:
        (node, lr) = i.split(" = ")
        (l, r) = lr.split(", ")
        path[node] = (l[1:], r[:-1])
    print(part1(path, instructions, "AAA", lambda x: x == "ZZZ"))
    print(part2(path, instructions))
