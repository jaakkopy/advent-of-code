def gen_points(guide):
    points = [(0, 0)]
    for g in guide:
        p = points[-1]
        d = int(g[1])
        match g[0]:
            case 'R': points.extend([(p[0], p[1] + x) for x in range(1, d+1)])
            case 'D': points.extend([(p[0] + y, p[1]) for y in range(1, d+1)])
            case 'L': points.extend([(p[0], p[1] - x) for x in range(1, d+1)])
            case 'U': points.extend([(p[0] - y, p[1]) for y in range(1, d+1)])
    return points


def calculate_area(points):
    s = 0
    for i in range(1, len(points)):
        s += (points[i][0] + points[i-1][0]) * (points[i-1][1] - points[i][1])
    i = 0.5 * abs(s) + 1 - len(points)/2
    return int(i + len(points))


if __name__ == "__main__":
    from sys import stdin
    guide = [x.rstrip().split() for x in stdin.readlines()]
    points = gen_points(guide)
    print(calculate_area(points))
