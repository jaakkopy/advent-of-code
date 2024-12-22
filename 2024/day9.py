def part1(block_map, free):
    file_ids = list(block_map.keys())
    for key in file_ids[::-1]:
        # move blocks to the first free slots
        ind = block_map[key]
        i = len(ind) - 1
        while i >= 0 and len(free) > 0:
            bi = ind[i]
            # Only replace with free blocks on the left
            if free[0] < bi:
                ind[i] = free[0]
                free.pop(0)
                free.append(bi)
            i -= 1
    checksum = sum([key * v for (key,val) in block_map.items() for v in val])
    print(checksum)


def part2(block_map, free):
    file_ids = list(block_map.keys())
    for key in file_ids[::-1]:
        ok = False
        ind = block_map[key]
        # Can we move the whole file?
        numblocks = len(ind)
        prev = free[0]
        c = [prev]
        for k in range(1, len(free)):
            if free[k] == prev + 1:
                c.append(free[k])
                prev = free[k]
            else:
                # if enough space was found:
                if len(c) >= numblocks:
                    ok = True
                    break
                prev = free[k]
                c = [prev]

        if not ok:
            continue

        # There is enough space, so move the file
        i = len(ind) - 1
        while i >= 0 and len(c) > 0 and c[0] < ind[i]:
            bi = ind[i]
            ind[i] = c[0]
            k = c.pop(0)
            free.remove(k)
            free.append(bi)
            i -= 1

        # make sure to keep the free space in order
        free = sorted(free)

    checksum = sum([key * v for (key,val) in block_map.items() for v in val])
    print(checksum)


if __name__ == "__main__":
    from sys import stdin
    from copy import deepcopy

    blocks = [int(x) for x in list(stdin.readline().strip())]
    block_map = {}
    block_index = 0
    free = []
    # Map file ids to block ids:
    for i in range(0, len(blocks), 2):
        key = i//2
        ind = block_map.setdefault(key, [])
        for j in range(blocks[i]):
            ind.append(block_index)
            block_index += 1
        if i + 1 < len(blocks):
            for j in range(blocks[i+1]):
                free.append(block_index)
                block_index += 1

    part1(deepcopy(block_map), deepcopy(free))
    part2(block_map, free)