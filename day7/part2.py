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

    free_space = 70000000 - SIZES['/']
    needed_space = 30000000 - free_space

    print(f'We need to find: {needed_space} space')

    smallest_dir = SIZES['/']

    for dir in SIZES:
        if SIZES[dir] < smallest_dir and SIZES[dir] > needed_space:
            smallest_dir = SIZES[dir]


    print(f"Smallest dir size: {smallest_dir}")