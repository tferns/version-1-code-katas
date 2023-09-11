area1 = [
    ["*", ".", ".", "."],
    [".", ".", ".", "."],
    [".", "*", ".", "."],
    [".", ".", ".", "."]
]

result_area1 = [
    ["*", "1", "0", "0"],
    ["2", "2", "1", "0"],
    ["1", "*", "1", "0"],
    ["1", "1", "1", "0"]
]

area2 = [
    ["*", "*", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", "*", ".", ".", "."]
]

result_area2 = [
    ['*', '*', '1', '0', '0'],
    ['3', '3', '2', '0', '0'],
    ['1', '*', '1', '0', '0']
]

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

def solve_minesweeper(area: list[list[str]]):
    num_rows = len(area)
    num_columns = len(area[0])

    for row in range(num_rows):
        for column in range(num_columns):
            value = area[row][column]
            if value != ".":
                continue

            bomb_count = 0
            for dr, dc in directions:
                new_row, new_col = row + dr, column + dc
                if 0 <= new_row < num_rows and 0 <= new_col < num_columns:
                    if area[new_row][new_col] == "*":
                        bomb_count += 1

            area[row][column] = str(bomb_count)

    import pprint
    pprint.pprint(area)
            
    return area

if __name__ == '__main__':
    print("Solving area 1:")
    assert solve_minesweeper(area1) == result_area1
    print()
    print("Solving area 2:")
    assert solve_minesweeper(area2) == result_area2
    print()
    print("Success! No errors :D")
