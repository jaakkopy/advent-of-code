def p1(line):
    (syms, nums) = line.split()
    nums = [int(x) for x in nums.split(',')]
    ls = len(syms)
    quests = [i for i in range(ls) if syms[i] == '?']

    # Mark each # with a 1 bit
    starter_bs = 0
    for i in range(ls):
        if syms[i] == '#':
            starter_bs |= (1 << i)

    def verify(x):
        k = x
        for n in nums:
            while x != 0 and (x & 1) == 0:
                x >>= 1
            count = 0
            while (x & 1) == 1:
                x >>= 1
                count += 1
            if count != n:
                return False
        # the 1 bits should match exactly to the numbers
        if x != 0:
            return False
        return True

    def ways(k, i):
        if i == len(quests):
            return int(verify(k))
        return ways(k | (1 << quests[i]), i + 1) + ways(k, i + 1)

    return ways(starter_bs, 0)
    

if __name__ == "__main__":
    from sys import stdin
    lines = [x.rstrip() for x in stdin.readlines()]
    print(sum(map(p1, lines)))