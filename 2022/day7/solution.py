
def map_sizes(lines: list[str]) -> dict:
    sizes = {}
    dir_stack = []
    for l in lines:
        parts = l.split()
        if l.startswith('$ ls') or l.startswith('dir'):
            continue
        if l.startswith('$ cd'):
            target = parts[2]
            if target == '..':
                dir_stack.pop()
            else:
                dir_stack.append(target)
            continue
        key = tuple(dir_stack) 
        while key:
            sizes[key] = sizes.get(key, 0) + int(parts[0])
            key = key[:-1]
    return sizes 


if __name__ == "__main__":
    from sys import stdin
    lines = [x.rstrip() for x in stdin.readlines()]
    # Part 1
    sizes = map_sizes(lines)
    print(sum(x for x in sizes.values() if x <= 100000))
    # Part 2
    available_size = 70000000 - sizes[('/',)]
    need_to_free = 30000000 - available_size
    print(min(filter(lambda v: v >= need_to_free, sizes.values())))