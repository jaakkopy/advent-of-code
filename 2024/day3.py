from sys import stdin

# State machines. Maybe a little crude but works in linear time...

class MulState:
    def __init__(self):
        self.state_trans = {
            -1: lambda x: 'm' if x == 'm' else None,
            'm': lambda x: 'u' if x == 'u' else None,
            'u': lambda x: 'l' if x == 'l' else None,
            'l': lambda x: '(' if x == '(' else None,
            '(': lambda x: 'd1' if x.isdigit() else None,
            'd1': lambda x: 'd1' if x.isdigit() else ',' if x == ',' else None,
            ',':  lambda x: 'd2' if x.isdigit() else None,
            'd2': lambda x: 'd2' if x.isdigit() else ')' if x == ')' else None
        }
        self.reset()
    
    def reset(self):
        self.s = -1
        self.d1 = ''
        self.d2 = ''

    def final(self):
        return self.s == ')'

    def result(self):
        return int(self.d1)*int(self.d2)

    def update(self, c):
        next_state = self.state_trans[self.s](c)
        if next_state is not None:
            self.s = next_state
            if self.s == 'd1':
                self.d1 += c
            if self.s == 'd2':
                self.d2 += c
            return True
        return False


class DoState:
    def __init__(self):
        self.state_trans = {
            -1: lambda x: 'd' if x == 'd' else None,
            'd': lambda x: 'o' if x == 'o' else None,
            'o': lambda x: 'n' if x == 'n' else '(' if x == '(' else None,
            'n': lambda x: "'" if x == "'" else None,
            "'": lambda x: 't' if x == 't' else None,
            't': lambda x: '(' if x == '(' else None,
            '(': lambda x: ')' if x == ')' else None
        }        
        self.reset()

    def reset(self):
        self.s = -1
        self.multiplier = 1

    def final(self):
        return self.s == ')'
    
    def result(self):
        return self.multiplier

    def update(self, c):
        next_state = self.state_trans[self.s](c)
        if next_state is not None:
            self.s = next_state
            if self.s == 'n':
                self.multiplier = 0
            return True
        return False


if __name__ == "__main__":
    l = stdin.readlines()
    chars = ''.join(l)

    cntr1 = 0
    cntr2 = 0
    mult = 1
    M = MulState()
    D = DoState()
    for c in chars:
        if not D.update(c):
            D.reset()
        if D.final():
            mult = D.result()
            D.reset()
        if not M.update(c):
            M.reset()
        if M.final():
            cntr1 += M.result()
            cntr2 += mult * M.result()
            M.reset()
    print(cntr1)
    print(cntr2)
