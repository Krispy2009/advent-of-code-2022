from pprint import pprint
import math

def read_input(filename):
    grid = []
    with open(filename) as f:
        for line in f.readlines():
            line = [int(i) for i in line.strip()]
            grid.append(line)
    return grid


def calc_viewing_distance(height, row, col, grid):
    direction_scores = []

    if row == 0 or col == 0 or row == len(grid)-1 or col == len(grid[row])-1:
        return 0

    #check left
    count = 0
    for i in range(col-1, -1, -1):
        count += 1
        if height <= grid[row][i]:
            direction_scores.append(count)
            break
    if len(direction_scores) < 1:
        direction_scores.append(count)

    
    #check right
    count = 0
    for i in range(col+1, len(grid[row])):
        count += 1
        if height <= grid[row][i]:
            direction_scores.append(count)
            break

    if len(direction_scores) < 2:
        direction_scores.append(count)

    #check top
    count = 0
    for i in range(row-1, -1, -1):
        count += 1
        if height <= grid[i][col]:
            direction_scores.append(count)
            break

    if len(direction_scores) < 3:
        direction_scores.append(count)

    #check bottom
    count = 0
    for i in range(row+1, len(grid)):
        count += 1
        if height <= grid[i][col]:
            direction_scores.append(count)
            break

    if len(direction_scores) < 4:
        direction_scores.append(count)

    return math.prod(direction_scores)



if __name__ == "__main__":
    grid = read_input('input.txt')
    highest = 0
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            distance = calc_viewing_distance(y, i, j, grid)
            if distance > highest:
                highest = distance
    print(f"Highest distance: {highest}")
