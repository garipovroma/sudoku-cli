from random import randint as rand

base_grid = [[2, 3, 8, 9, 6, 5, 7, 1, 4],
             [7, 5, 9, 4, 1, 3, 6, 8, 2],
             [4, 1, 6, 2, 7, 8, 9, 5, 3],
             [9, 4, 5, 1, 3, 6, 2, 7, 8],
             [6, 8, 7, 5, 2, 4, 1, 3, 9],
             [3, 2, 1, 8, 9, 7, 4, 6, 5],
             [1, 6, 2, 3, 5, 9, 8, 4, 7],
             [5, 7, 4, 6, 8, 2, 3, 9, 1],
             [8, 9, 3, 7, 4, 1, 5, 2, 6]]


def transpose(grid):
    return [[grid[j][i] for j in range(len(grid[0]))] for i in range(len(grid))]


def light_swap_rows(grid):
    result = grid
    subfield_x = rand(0, 2)
    a = rand(0, 2)
    b = (a + rand(1, 2)) % 3
    line_a = subfield_x * 3 + a
    line_b = subfield_x * 3 + b
    result[line_a], result[line_b] = result[line_b], result[line_a]
    return result


def light_swap_columns(grid):
    result = grid
    result = transpose(result)
    result = light_swap_rows(result)
    result = transpose(result)
    return result


def heavy_swap_rows(grid):
    result = grid
    a = rand(0, 2)
    b = (a + rand(1, 2)) % 3
    lines_a = result[a * 3:(a + 1) * 3]
    lines_b = result[b * 3:(b + 1) * 3]
    lines_a, lines_b = lines_b, lines_a
    for i in range(3):
        result[a * 3 + i] = lines_a[i]
        result[b * 3 + i] = lines_b[i]
    return result


def heavy_swap_columns(grid):
    result = grid
    result = transpose(result)
    result = heavy_swap_rows(result)
    result = transpose(result)
    return result


def print(grid):
    y = 0
    for i in grid:
        if (y % 3 == 0):
            print()
        y += 1
        x = 0
        for j in i:
            if x % 3 == 0:
                print(" ", end="")
            print(j, end=" ")
            x += 1
        print()

    print()
    return None


def generate(deleted_cells_num):
    result = base_grid
    iterations_num = rand(0, 500)
    for i in range(iterations_num):
        transform_type = rand(1, 5)
        if transform_type == 1:
            transpose(result)
        elif transform_type == 2:
            light_swap_rows(result)
        elif transform_type == 3:
            light_swap_columns(result)
        elif transform_type == 4:
            heavy_swap_rows(result)
        elif transform_type == 5:
            heavy_swap_columns(result)
    for i in range(deleted_cells_num):
        x = rand(0, 8)
        y = rand(0, 8)
        result[x][y] = 0
    return result
