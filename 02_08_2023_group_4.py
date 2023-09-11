sudoku_ok = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],  # 0 - 2
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9]
]

sudoku_bad = [
    [4, 5, 3, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9]
]


def is_sudoku_valid(sudoku: list[list[int]]) -> bool:
    for column in sudoku:
        if len(set(column)) != 9:
            return False

    transposed = [list(column) for column in zip(*sudoku)]
    for column in transposed:
        if len(set(column)) != 9:
            return False

    # for column in range(0, 9, 3):
    #     for row in range(0, 9, 3):
    #         top_left_coord = (column, row)
    #         ...

    import numpy
    numpy_arr = numpy.array(sudoku)
    # potential bug in here, reshape hasn't been done properly.
    reshaped = numpy_arr.reshape(3, 3, 3, 3).reshape(9, 9)
    # reshaped = numpy_arr.reshape(9, 3, 3)
    # import pprint
    # pprint.pprint(reshaped)
    for column in reshaped:
        if len(set(column)) != 9:
            return False

    return True


if __name__ == '__main__':
    assert is_sudoku_valid(sudoku_ok) is True, "first sudoku is valid"
    assert is_sudoku_valid(sudoku_bad) is False, "second sudoku is valid"
    print("Didn't raise an error, so it worked?...")
