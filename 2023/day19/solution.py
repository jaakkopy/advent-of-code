from dataclasses import dataclass
import operator


@dataclass
class Part():
    x: int
    m: int
    a: int
    s: int


def eval_condition(cond: str, part: Part) -> bool:
    op = None
    num = None
    var = None
    if '<' in cond:
        (var, num) = cond.split("<")
        num = int(num)
        op = operator.lt
    elif '>' in cond:
        (var, num) = cond.split(">")
        num = int(num)
        op = operator.gt

    if op is not None:
        match var:
            case 'x': return op(part.x, num)
            case 'm': return op(part.m, num)
            case 'a': return op(part.a, num)
            case 's': return op(part.s, num)

    return True


def is_accepted(key: str, workflows: dict[str], part: Part):
    if key == 'A':
        return True
    elif key == 'R':
        return False
    conditions = workflows[key]
    i = 0
    while i < len(conditions):
        ok = eval_condition(conditions[i][0], part)
        if ok:
            return is_accepted(conditions[i][-1], workflows, part)
        i += 1
    return is_accepted(conditions[i][-1], workflows, part)


if __name__ == "__main__":
    from sys import stdin
    [workflows, parts] = stdin.read().split('\n\n')
    workflows = [x.split('{') for x in workflows.splitlines()]
    workflows = {x[0]: [y.split(':') for y in x[1][:-1].split(',')]
                 for x in workflows}
    parts = [Part(*[int(y.split('=')[1]) for y in x[1:-1].split(',')])
             for x in parts.splitlines()]
    s = 0
    for p in parts:
        if is_accepted('in', workflows, p):
            s += p.x + p.m + p.a + p.s
    print(s)
