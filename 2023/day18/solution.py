def gen_points(guide):
    points = [(0, 0)]
    for g in guide:
        p = points[-1]
        d = int(g[1])
        match g[0]:
            case 'R': points.append((p[0], p[1] + d))
            case 'D': points.append((p[0] + d, p[1]))
            case 'L': points.append((p[0], p[1] - d))
            case 'U': points.append((p[0] - d, p[1]))
    return points


def calculate_area(points):
    s = 0
    b = 0
    for i in range(1, len(points)):
        b += abs(points[i-1][0] - points[i][0]) + abs(points[i-1][1] - points[i][1])
        s += (points[i][0] + points[i-1][0]) * (points[i-1][1] - points[i][1])
    i = 0.5 * abs(s) + 1 - b/2
    return int(i + b)


if __name__ == "__main__":
    from sys import stdin
    guide = [x.rstrip().split() for x in stdin.readlines()]
    points = gen_points(guide)
    print(calculate_area(points))
