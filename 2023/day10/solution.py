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

def find_farthest_away(G, start):
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

def find_loop(G, start):
    rows = len(G)
    cols = len(G[0])
    step = next(get_allowed_positions(start, G[start[0]][start[1]], rows, cols))
    visited = set([start, step]) # Begin the cycle by taking a step in any path from the starting position
    S = [step]
    path = [start]
    while len(S) > 0:
        v = S.pop()
        path.append(v)
        for pos in get_allowed_positions(v, G[v[0]][v[1]], rows, cols):
            if pos not in visited:
                visited.add(pos)
                S.append(pos)
    return path

def find_area_inside_loop(G, start):
    '''
    A = 1/2 * |sum( (y_i+1 + y_i)*(x_i - x_i+1))| where the points are in counter clockwise or clockwise order: https://en.wikipedia.org/wiki/Shoelace_formula
    A = i + b/2 - 1 for integer coordinates where i = interior points and b = points on the border: https://en.wikipedia.org/wiki/Pick%27s_theorem
    
    solve for i:
    i + b/2 - 1 = 1/2 * sum( (y_i+1 + y_i)*(x_i - x_i+1))  
    i = 1/2 * sum( (y_i+1 + y_i)*(x_i - x_i+1)) - b/2 + 1
    '''
    loop = find_loop(G, start)
    s = 0
    for i in range(0, len(loop)-1):
        s += (loop[i+1][0] + loop[i][0])*(loop[i][1] - loop[i+1][1]) 
    s  = abs(s/2)
    return s - len(loop)/2 + 1

if __name__ == "__main__":
    from sys import stdin
    lines = [x.rstrip() for x in stdin.readlines()]
    G, start = make_graph(lines)
    max_dist = find_farthest_away(G, start)
    print(max_dist) # Part 1
    a = find_area_inside_loop(G, start)
    print(a)