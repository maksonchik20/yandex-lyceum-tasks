from copy import deepcopy


def get_variants(sudoku):
    variants = []
    for i, row in enumerate(sudoku):
        for j, value in enumerate(row):
            if not value:
                row_values = set(row)
                column_values = set([sudoku[k][j] for k in range(4)])
                sq_y = i // 2
                sq_x = j // 2
                square3x3_values = set([
                    sudoku[m][n]
                    for m in range(sq_y * 2, sq_y * 2 + 2)
                    for n in range(sq_x * 2, sq_x * 2 + 2)
                ])
                exists = row_values | column_values | square3x3_values
                values = set(range(1, 5)) - exists
                variants.append((i, j, values))

    return variants


def solve(sudoku):
    if all([k for row in sudoku for k in row]):
        return sudoku

    variants = get_variants(sudoku)

    x, y, values = min(variants, key=lambda x: len(x[2]))

    for v in values:
        new_sudoku = deepcopy(sudoku)
        new_sudoku[x][y] = v
        s = solve(new_sudoku)
        if s:
            return s
    return None


print(*["".join(map(str, el)) for el in solve([
        list(map(int, input().strip())),
        list(map(int, input().strip())),
        list(map(int, input().strip())),
        list(map(int, input().strip()))
        ])], sep='\n')