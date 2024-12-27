def f(x: int):
    '''
    f(x) = (1), if x = 0
    f(x) = (a, b) if |x|%2 = 0, where x=ab
    f(x) = 2024*x, otherwise
    '''
    if x == 0:
        return (1,)
    s = str(x)
    l = len(s)
    if l % 2 == 0:
        return (int(s[0:l//2]), int(s[l//2:]))
    return (2024*x,)


def blink(x, memo={}, blinks=25):
    if blinks <= 0:
        return 1
    if (x, blinks) in memo:
        return memo[(x, blinks)]
    stones = 0
    for y in f(x):
        stones += blink(y, memo, blinks - 1)
    memo[(x, blinks)] = stones
    return stones


if __name__ == "__main__":
    from sys import stdin

    nums = [int(x) for x in stdin.readline().strip().split()]
    stones1 = 0
    stones2 = 0
    memo = {}
    for x in nums:
        stones1 += blink(x, memo, 25)
        stones2 += blink(x, memo, 75)

    print(stones1)
    print(stones2)