from collections import deque

ELEVATIONS = 'abcdefghijklmnopqrstuvwxyz'
def read_input(filename):
    global S
    global E

    grid = []
    with open(filename) as f:
        for i, line in enumerate(f.readlines()):
            line = line.strip()
            row = []
            for j, char in enumerate(list(line)):
                if char == 'S':
                    char = 'a'
                    S = (i,j)
                elif char == 'E':
                    char = 'z'
                    E = (i,j)
                row.append(ELEVATIONS.index(char))
            grid.append(row)
    return grid


if __name__ == "__main__":
    global S
    global E
    grid = read_input('input.txt')


    height = len(grid)
    width = len(grid[0])
    min_distance = 999999999999
    
    for h in range(height):
        for w in range(width):
            if grid[h][w] == 0:
                #only check 'a'
                queue = deque([(h, w, 0)])
                visited = set()

                while queue:
                    x, y, distance = queue.popleft()
                    
                    if distance > min_distance:
                        continue

                    if (x,y) == E:
                        print(f"({h},{w}) - hops: {distance}")
                        if distance < min_distance:
                            min_distance = distance
                        break

                    elif (x,y) in visited:
                        continue

                    visited.add((x,y))

                    for i in range(x-1, x+2):
                        for j in range(y-1, y+2):
                            if i in range(0, height) and j in range(0, width):
                                if i == x or j == y:
                                    if grid[x][y]+1 >= grid[i][j]:
                                        queue.append((i, j, distance+1))
                    
        