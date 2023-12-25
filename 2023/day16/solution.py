def in_bounds(rows, cols, r, c):
    return (r >= 0 and r < rows) and (c >= 0 and c < cols)


def up(pos_and_dir, p, d):
    pos_and_dir.append(((p[0] - 1, p[1]), (-1, 0)))


def down(pos_and_dir, p, d):
    pos_and_dir.append(((p[0] + 1, p[1]), (1, 0)))


def left(pos_and_dir, p, d):
    pos_and_dir.append(((p[0], p[1] - 1), (0, -1)))


def right(pos_and_dir, p, d):
    pos_and_dir.append(((p[0], p[1] + 1), (0, 1)))


def vertical_pipe(pos_and_dir, p, d):
    # |
    up(pos_and_dir, p, d)
    down(pos_and_dir, p, d)


def horizontal_pipe(pos_and_dir, p, d):
    # -
    left(pos_and_dir, p, d)
    right(pos_and_dir, p, d)


def mirror1(pos_and_dir, p, d):
    # \
    if d[1] == 1:
        down(pos_and_dir, p, d)
    elif d[1] == -1:
        up(pos_and_dir, p, d)
    elif d[0] == 1:
        right(pos_and_dir, p, d)
    elif d[0] == -1:
        left(pos_and_dir, p, d)


def mirror2(pos_and_dir, p, d):
    # /
    if d[1] == 1:
        up(pos_and_dir, p, d)
    elif d[1] == -1:
        down(pos_and_dir, p, d)
    elif d[0] == 1:
        left(pos_and_dir, p, d)
    elif d[0] == -1:
        right(pos_and_dir, p, d)


def follow_light_paths(lines: list[str], startpos, startdir):
    rows = len(lines)
    cols = len(lines[0])
    visited = set()
    pos_and_dir = [(startpos, startdir)]
    while len(pos_and_dir) > 0:
        pd = pos_and_dir.pop()
        (p, d) = pd
        (r, c) = p
        if pd in visited or not in_bounds(rows, cols, r, c):
            continue
        visited.add(pd)
        if lines[r][c] == '|' and d[1] != 0:
            vertical_pipe(pos_and_dir, p, d)
        elif lines[r][c] == '-' and d[0] != 0:
            horizontal_pipe(pos_and_dir, p, d)
        elif lines[r][c] == '\\':
            mirror1(pos_and_dir, p, d)
        elif lines[r][c] == '/':
            mirror2(pos_and_dir, p, d)
        else:
            nextpd = ((p[0] + d[0], p[1] + d[1]), d)
            if in_bounds(rows, cols, nextpd[0][0], nextpd[0][1]):
                pos_and_dir.append(nextpd)
    return visited


if __name__ == "__main__":
    from sys import stdin
    lines = [list(x.rstrip()) for x in stdin.readlines()]
    markers = [x.copy() for x in lines]
    visited = follow_light_paths(lines, (0, 0), (0, 1))
    unique_positions = len(set([x[0] for x in visited]))
    print(unique_positions)  # part 1
    highest_energy = 0
    for c in range(len(lines[0])):
        highest_energy = max(
            highest_energy, len(
                set([x[0] for x in follow_light_paths(
                    lines, (0, c), (1, 0))]))
        )
        highest_energy = max(
            highest_energy, len(
                set([x[0] for x in follow_light_paths(
                    lines, (len(lines) - 1, c), (-1, 0))]))
        )
    for r in range(len(lines)):
        highest_energy = max(
            highest_energy, len(
                set([x[0] for x in follow_light_paths(
                    lines, (r, 0), (0, 1))]))
        )
        highest_energy = max(
            highest_energy, len(
                set([x[0] for x in follow_light_paths(
                    lines, (r, len(lines[0]) - 1), (0, -1))]))
        )
    print(highest_energy)  # part 2
