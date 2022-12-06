# MARK_LENGTH = 4
MARK_LENGTH = 14

def read_input(filename):
    lines = []
    with open(filename) as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines
    


def find_mark(line):
    index = MARK_LENGTH
    while index < len(line):
        sub_str =  line[index-MARK_LENGTH:index]
        if is_mark(sub_str):
            print(f'mark found at index: {index}')
            break
        index +=1

def is_mark(sub_str):
    return len(set(list(sub_str))) == MARK_LENGTH

if __name__ == "__main__":
    lines = read_input('input.txt')
    for line in lines:
        find_mark(line)