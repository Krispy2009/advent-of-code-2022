def read_input(filename):
    instructions = []
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            direction, moves = line.split()
            instructions.append((direction, int(moves)))

    return instructions

def apply_move(position, direction):

    if direction == 'U':
        position[1] -= 1
    elif direction == 'D':
        position[1] += 1
    elif direction == 'L':
        position[0] -= 1
    elif direction == 'R':
        position[0] += 1

    return position



def find_x_distance(head, tail):
    return abs(head[0]-tail[0])

def find_y_distance(head, tail):
    return abs(head[1]-tail[1])



if __name__ == "__main__":
    instructions = read_input('input.txt')
    
    visited = set()

    head = [0,0]
    tail = [0,0]

    visited.add(tuple(tail))

    for instruction in instructions:
        direction, moves = instruction
        for i in range(moves):
            # print(f"{direction} {i}")
            head = apply_move(head, direction)
            if find_x_distance(head, tail) + find_y_distance(head, tail) == 3:
                #move tail diagonally
                # print('move diagonally')
                if head[0] - tail[0] == 2:
                    # print('>vv')
                    tail[0] += 1
                    tail[1] += head[1] - tail[1]
                    visited.add(tuple(tail))
                if tail[0] - head[0] == 2:
                    # print('<^^')
                    tail[0] -= 1
                    tail[1] -= tail[1] - head[1]
                    visited.add(tuple(tail))
                if head[1] - tail[1] == 2:
                    # print('v>>')
                    tail[1] += 1
                    tail[0] += head[0] - tail[0]
                    visited.add(tuple(tail))
                if tail[1] - head[1] == 2:
                    # print('^>>')
                    tail[1] -= 1
                    tail[0] -= tail[0] - head[0]
                    visited.add(tuple(tail))
            else:
                if head[0] - tail[0] == 2:
                    tail[0] +=1
                    visited.add(tuple(tail))
                if tail[0] - head[0] == 2:
                    tail[0] -=1
                    visited.add(tuple(tail))
                if head[1] - tail[1] == 2:
                    tail[1] +=1
                    visited.add(tuple(tail))
                if tail[1] - head[1] == 2:
                    tail[1] -=1
                    visited.add(tuple(tail))
            # print(f"{head} H ---  T {tail}")
                    
    
    print(f"Visited: {len(visited)}")
