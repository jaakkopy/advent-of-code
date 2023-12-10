D = {
    # north, east, south, west
    '|': 0b1010,
    '-': 0b0101,
    'L': 0b1100,
    'J': 0b1001,
    '7': 0b0011,
    'F': 0b0110,
    '.': 0b0000,
    'S': 0b0000
}

def make_graph(lines):
    G = []
    start = None
    for r in range(len(lines)):
        row = []
        for c in range(len(lines[r])):
            row.append(D[lines[r][c]])
            if lines[r][c] == 'S':
                start = (r,c)
        G.append(row)
    dirs = 0
    (r,c) = start
    rows = len(G)
    cols = len(G[0])
    if r+1 < rows and G[r+1][c] & 0b1000:
        dirs |= 0b0010
    if r-1 >= 0 and G[r-1][c] & 0b0010:
        dirs |= 0b1000
    if c-1 >= 0 and G[r][c-1] & 0b0100:
        dirs |= 0b0001
    if c+1 < cols and G[r][c+1] & 0b0001:
        dirs |= 0b0100
    G[r][c] = dirs
    return G, start

def get_allowed_positions(v, pipe_type, r, c):
    if pipe_type & 0b0001 and v[1] - 1 >= 0:
        yield (v[0], v[1] - 1)
    if pipe_type & 0b0100 and v[1] + 1 < c:
        yield (v[0], v[1] + 1)
    if pipe_type & 0b0010 and v[0] + 1 < r:
        yield (v[0] + 1, v[1])
    if pipe_type & 0b1000 and v[0] - 1 >= 0:
        yield (v[0] - 1, v[1])

def bfs(G, start):
    rows = len(G)
    cols = len(G[0])
    visited = set([start])
    Q = [(start, 0)]
    max_dist = 0
    while len(Q) > 0:
        v, dist = Q.pop(0)
        max_dist = max(max_dist, dist)
        for pos in get_allowed_positions(v, G[v[0]][v[1]], rows, cols):
            if pos not in visited:
                visited.add(pos)
                Q.append((pos, dist + 1))
    return max_dist


if __name__ == "__main__":
    from sys import stdin
    lines = [x.rstrip() for x in stdin.readlines()]
    G, start = make_graph(lines)
    print(bfs(G, start))
