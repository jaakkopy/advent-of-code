def tilt_vertical(lines, direction):
    rows = len(lines)
    cols = len(lines[0])
    (start, end, inc) = (0, rows, 1) if direction == -1 else (rows - 1, -1, -1)
    s = 0
    for r in range(start, end, inc):
        for c in range(cols):
            if lines[r][c] == 'O':
                pos = r + direction
                while (pos >= 0 and pos < rows) and lines[pos][c] == '.':
                    lines[pos][c], lines[pos-direction][c] = lines[pos-direction][c], lines[pos][c]
                    pos += direction
                s += rows - (pos - direction)
    return s


def tilt_horizontal(lines, direction):
    rows = len(lines)
    cols = len(lines[0])
    (start, end, inc) = (0, cols, 1) if direction == -1 else (cols - 1, -1, -1)
    s = 0
    for c in range(start, end, inc):
        for r in range(rows):
            if lines[r][c] == 'O':
                pos = c + direction
                while (pos >= 0 and pos < cols) and lines[r][pos] == '.':
                    lines[r][pos], lines[r][pos-direction] = lines[r][pos-direction], lines[r][pos]
                    pos += direction
                s += rows - r
    return s


def full_rotation(lines):
    tilt_vertical(lines, -1)
    tilt_horizontal(lines, -1)
    tilt_vertical(lines, 1)
    return tilt_horizontal(lines, 1)


if __name__ == "__main__":
    from sys import stdin
    lines = [list(x.rstrip()) for x in stdin.readlines()]
    original = [x.copy() for x in lines]

    s = tilt_vertical(lines, -1)
    print(s)  # part 1

    lines = [x.copy() for x in original]
    seen_before = {}
    as_tuple = tuple([tuple(x) for x in lines])
    counter = 0
    while as_tuple not in seen_before:
        seen_before[as_tuple] = counter
        s = full_rotation(lines)
        counter += 1
        as_tuple = tuple([tuple(x) for x in lines])

    cycle_start = seen_before[as_tuple]
    cycle_end = counter
    steps = cycle_end - cycle_start

    remaining = (1000000000 - cycle_start) % steps
    for _ in range(remaining):
        s = full_rotation(lines)
    print(s)  # part 2
