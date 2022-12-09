from pprint import pprint
from collections import defaultdict

DIR_STACK= []
SIZES = defaultdict(int)
def read_input(filename):
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith('$ cd'):
                _, curr_dir = line.split('$ cd ')
                if curr_dir == '..':
                   curr_dir = DIR_STACK.pop()
                else:
                    DIR_STACK.append(curr_dir)

            elif line.startswith('$ ls'):
                continue
            elif not line.startswith('$'):
                if not line.startswith('dir'):
                    size, _ = line.split(' ')
                    for i in range(len(DIR_STACK)):
                        SIZES[''.join(DIR_STACK[:i+1])] += int(size)


if __name__ == "__main__":
    read_input('input.txt')

    total_size = 0

    for dir in SIZES:
        if SIZES[dir] < 100000:
            total_size += SIZES[dir]

    print(f"\n Sum: {total_size}")
