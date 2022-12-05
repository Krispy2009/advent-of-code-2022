from collections import deque
def read_input(filename):

    moves = []
    positions = []
    stacks = {}

    with open(filename) as f:
        for line in f.readlines():
            line = line.replace('\n','')

            if line.startswith('move'):
                line = line.replace('move','').replace('from','').replace('to','').split()
                line = tuple(int(i) for i in line)
                moves.append(line)
            elif line.startswith(' 1'):
                number_of_stacks = int(line[-2])
                print(f'there are {number_of_stacks} stacks')
                stacks = {k: deque() for k in range(1,number_of_stacks+1)}
            elif line != '':
                positions.append(line)

    for line in positions:
        for i, char in enumerate(line):
            if char == '[':
                stack_id = translate_index_to_stack_id(i+1)
                stacks[stack_id].insert(0, line[i+1])
        print(stacks)
    return stacks, moves


def apply_move(stacks, move):
    # (1, 2, 1) = move 1 from 2 to 1
    num, start, end = move

    while num > 0:
        temp = stacks[start].pop()
        stacks[end].append(temp)

        num -=1
    return stacks

def translate_index_to_stack_id(index):
    return int((index - 1)/4 ) + 1


if __name__ == "__main__":
    stacks, moves = read_input('input.txt')

    for move in moves:
        stacks = apply_move(stacks, move)

    for i in stacks:
        # print(f"{i}: {stacks[i][-1]}")
        print(stacks[i][-1], end='')