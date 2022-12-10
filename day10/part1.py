
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
    elif line[0] == 'addx':
        CYCLES.append(X)
        CYCLE_COUNT += 1
        print(f'During cycle {CYCLE_COUNT}, X = {X}')
        CYCLES.append(X)
        CYCLE_COUNT += 1
        print(f'During cycle {CYCLE_COUNT}, X = {X}')
        X += line[1]
        # CYCLES.append(X)

if __name__ == "__main__":
    program = read_input('input.txt')
    X = 1
    CYCLES = []
    CYCLE_COUNT = 0
    for line in program:
        execute(line)
        print(f'After  cycle {CYCLE_COUNT}, X = {X}')
    CYCLES.append(X)
    print(CYCLES)

    if len(CYCLES) > 19:
        s = 0
        positions = [20, 60, 100, 140, 180, 220]
        for p in positions:
            s += CYCLES[p-1] * p
        print(f"Signal strength sum: {s}")