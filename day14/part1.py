def read_input(filename):

    grid_instructions = []

    with open(filename) as f:
        for row in f.readlines():
            points = [point.split(',') for point in row.strip().split(' -> ') ]
            points = [(int(x), int(y)) for x,y in points]
            grid_instructions.append(points)
    print(grid_instructions)

    return grid_instructions


def translate(x,y):
    min_x = min([i[0] for instruction in instructions for i in instruction])
    min_y = min([i[1] for instruction in instructions for i in instruction])

    return x - min_x, y - min_y


def print_grid(instructions):
    max_x = max([i[0] for instruction in instructions for i in instruction])
    max_y = max([i[1] for instruction in instructions for i in instruction])

    max_x, _ = translate(max_x, max_y)

    grid = []
    for i in range(max_y+1):
        row = ['.'] * (max_x+1)
        grid.append(row)
    print(len(grid))

    for instruction in instructions:
        print('++ new line ++')
        for i in range(len(instruction)-1):
            print(f"Adding rock: {instruction[i]} -> {instruction[i+1]}")
            start_x, start_y = instruction[i]
            end_x, end_y = instruction[i+1]

            start_x, _ = translate(start_x, start_y)
            end_x, _ = translate(end_x, end_y)

            if start_x > end_x:
                start_x, end_x = end_x, start_x

            if start_y > end_y:
                start_y, end_y = end_y, start_y

            for x in range(start_x, end_x+1):
                grid[start_y][x] = '#'
            for y in range(start_y, end_y+1):
                grid[y][start_x] = '#'


    pretty(grid)
    return grid


def can_fall_down(grid, sand_y, sand_x):
    if grid[sand_y+1][sand_x] == '.':
        return True
    return False

def can_fall_down_left(grid, sand_y, sand_x):
    if grid[sand_y+1][sand_x-1] == '.':
        return True
    return False

def can_fall_down_right(grid, sand_y, sand_x):
    if grid[sand_y+1][sand_x+1] == '.':
        return True
    return False






def drop_sand(grid):
    sand_x, _ = translate(500, 0)
    sand_y = 0
    while True:
        if can_fall_down(grid, sand_y, sand_x):
            sand_y += 1
            print(f'Sand falls down to {sand_y}, {sand_x}')
            continue
        elif can_fall_down_left(grid, sand_y, sand_x):
            sand_y += 1
            sand_x -= 1
            print(f'Sand falls down left to {sand_y}, {sand_x}')
            continue
        elif can_fall_down_right(grid, sand_y, sand_x):
            sand_y += 1
            sand_x += 1
            print(f'Sand falls down right to {sand_y}, {sand_x}')
            continue
        else:
            print('cannot fall anymore')
            grid[sand_y][sand_x] = 'o'
            print(f'Sand settles at {sand_y}, {sand_x}')
            # pretty(grid)
            return grid


def pretty(grid):
    for line in grid:
        print(''.join(line))


instructions = read_input('input.txt')
grid = print_grid(instructions)

sand = 0
while True:
    try:
        grid = drop_sand(grid)
        sand += 1
    except:
        print(f"Dropped {sand} sand")
        break
