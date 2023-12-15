def compare_rows(rows, mid):
    for row in rows:
        i = mid
        j = mid + 1
        while i >= 0 and j < len(row):
            if row[i] != row[j]:
                return False
            i -= 1
            j += 1
    return True 

def compare_cols(rows, mid):
    for c in range(len(rows[0])):
        i = mid
        j = mid + 1
        while i >= 0 and j < len(rows):
            if rows[i][c] != rows[j][c]:
                return False
            i -= 1
            j += 1
    return True

def check_vertical_reflection(group):
    rows = len(group)
    cols = len(group[0])
    for mid in range(cols - 1):
        if compare_rows(group, mid):
            return mid + 1
    return 0 

def check_horizontal_reflection(group):
    rows = len(group)
    cols = len(group[0])
    for mid in range(rows - 1):
        if compare_cols(group, mid):
            return 100 * (mid + 1)
    return 0 

if __name__ == "__main__":
    from sys import stdin
    lines = [x.rstrip() for x in stdin.readlines()]
    groups = []
    g = []
    for l in lines:
        if l == '':
            groups.append(g)
            g = []
        else:
            g.append(l)
    groups.append(g)
    s = sum(map(lambda x: check_horizontal_reflection(x) + check_vertical_reflection(x), groups))
    print(s)