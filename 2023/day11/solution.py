def create_adjacency_matrix(M):
    rows = len(M)
    cols = len(M[0])
    nodes = []
    no_galaxy_rows = [True] * rows
    no_galaxy_cols = [True] * cols
    for r in range(rows):
        for c in range(cols):
            if M[r][c] == '#':
                no_galaxy_cols[c] = False
                no_galaxy_rows[r] = False
                galaxy = True
                nodes.append((r,c))
    l = len(nodes)
    D = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            if j == i:
                continue
            D[i][j] = abs(nodes[i][0] - nodes[j][0]) + abs(nodes[i][1] - nodes[j][1]) 
            # check if there is a no-galaxy column between the galaxies:
            startc = min(nodes[i][1], nodes[j][1])
            endc =  max(nodes[i][1], nodes[j][1]) + 1
            for c in range(startc, endc, 1):
                if no_galaxy_cols[c]:
                    D[i][j] += 1
            # check if there is a no-galaxy row between the galaxies:
            startr = min(nodes[i][0], nodes[j][0])
            endr =  max(nodes[i][0], nodes[j][0]) + 1
            for r in range(startr, endr, 1):
                if no_galaxy_rows[r]:
                    D[i][j] += 1
    return D 


if __name__ == "__main__":
    from sys import stdin
    M = [x.rstrip() for x in stdin.readlines()]
    D = create_adjacency_matrix(M)
    s = 0
    for v in range(len(D)):
        for u in range(v, len(D)):
            s += D[v][u]
    print(s) # part 1