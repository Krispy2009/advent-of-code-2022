from pprint import pprint

def read_input(filename):
    grid = []
    with open(filename) as f:
        for line in f.readlines():
            line = [int(i) for i in line.strip()]
            grid.append(line)
    return grid


def is_visible(height, row, col, grid):

    visible_directions = []

    if row == 0 or col == 0 or row == len(grid)-1 or col == len(grid[row])-1:
        return True

    #check left
    for i in range(col):
        if height <= grid[row][i]:
            visible_directions.append(False)
            break
    
    #check right
    for i in range(col+1, len(grid[row])):
        if height <= grid[row][i]:
            visible_directions.append(False)
            break

    #check top
    for i in range(row):
        if height <= grid[i][col]:
            visible_directions.append(False)
            break

    #check bottom
    for i in range(row+1, len(grid)):

        if height <= grid[i][col]:
            visible_directions.append(False)
            break
    
    # if len(visible_directions) == 4:
    #     print(f"=> {height} at ({row},{col}) is not visible")

    return len(visible_directions) < 4



if __name__ == "__main__":
    grid = read_input('input.txt')
    count = 0
    for i, x in enumerate(grid):
        for j, y in enumerate(x):
            if is_visible(y, i, j, grid):
                count +=1
                # print(f"{count}: {y} at ({i},{j}) is visible")

    print(count)