def to_upper_triangular(mat):

    print("Matrix given:")
    for row in mat:
        for col in row:
            print(col, end=" ")
        print()

    for r in range(len(mat)):

        pivot_row_index = r
        max_val_in_current_col = mat[r][pivot_row_index]

        for rr in range(r + 1, len(mat)):
            if (max_val_in_current_col < abs(mat[rr][r])):
                pivot_row_index = rr
                max_val_in_current_col = mat[rr][r]


        if mat[r][pivot_row_index] == 0:
            print("Matrix is singular; cannot be brought to upper triangular form")
            return

        if (pivot_row_index != r):
            for i in range(len(mat)+1):
                tmp=mat[r][i]
                mat[r][i] = mat[pivot_row_index][i]
                mat[pivot_row_index][i] = tmp


        for rr in range(r + 1, len(mat)):
            factor = mat[rr][r] / mat[r][r]
            for cc in range(r + 1, len(mat) + 1):
                mat[rr][cc] -= round(mat[r][cc] * factor, 2)

            mat[rr][r] = 0

    print("Transformed matrix:")
    for row in mat:
        for col in row:
            print(col, end=" ")
        print()


mat = [[2, 4, -2, 10],
       [4,-2,  6, 20],
       [6,-4,  2, 18]]

to_upper_triangular(mat)
