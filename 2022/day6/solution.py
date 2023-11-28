'''
Use a bit map to keep track of unique characters in sequence -> if the value increases length times in a row (added a 1 to the map every iteration), there were length amount of unique sequential characters.
If the value is not updated, remove added characters from the map starting from the left side of the window until the duplicate has been removed.
'''
def start_of_packet(line: str, length: int) -> int:
    counter = 0
    bit_map = 0
    l = 0
    char_num = lambda c: ord(c) - ord('a') 
    for i,c in enumerate(line):
        if counter == length:
            return i
        pos = (1 << char_num(c))
        b2 = bit_map | pos 
        if b2 > bit_map:
            counter += 1
            bit_map = b2
        else:
            while bit_map & pos > 0:
                bit_map = bit_map & ( ~(1 << char_num(line[l])) ) 
                l += 1
                counter -= 1
            bit_map |= pos
            counter += 1

if __name__ == "__main__":
    from sys import stdin
    message = stdin.read()
    # part 1
    print(start_of_packet(message, 4))
    # part 2
    print(start_of_packet(message, 14))