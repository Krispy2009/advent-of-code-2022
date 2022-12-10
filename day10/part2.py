
def read_input(filename):
    program = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip().split()
            if line[0] == 'addx':
                line[1] = int(line[1])
            program.append(line)

    return program

def execute(line):
    global CYCLES
    global CYCLE_COUNT
    global X
    if line[0] == 'noop':
        CYCLE_COUNT += 1
        CYCLES.append(X)
        print_crt(X)
 


    elif line[0] == 'addx':
        CYCLES.append(X)
        CYCLE_COUNT += 1
        print_crt(X)
        CYCLES.append(X)
        CYCLE_COUNT += 1
        print_crt(X)
        X += line[1]

def calc_sprite(X):
    return (X-1, X, X+1)

def print_crt(X):
    sprite = calc_sprite(X)
    if (CYCLE_COUNT-1)%40 in sprite:
        CRT[CYCLE_COUNT-1] = '#'

if __name__ == "__main__":
    program = read_input('input.txt')
    X = 1
    CYCLES = []
    CYCLE_COUNT = 0
    CRT = ['.'] * 240

    for line in program:
        execute(line)
    CYCLES.append(X) 
    print_crt(X)

    length = 40
    offset = 0
    for i in range(6):
        print(''.join(CRT[i*length:length+offset]))
        offset+=length
