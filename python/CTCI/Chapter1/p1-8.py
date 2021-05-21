# 1.8 Zero Matrix
# Write an algorithm such that if an element in an M x N matrix is 0, its entire row and
# column are set to 0.

# Not eligant. O(N^2)?
def Zero(matrix):
    zero_list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_list.append((i,j))

    for zero in zero_list:
        for i in range(len(matrix[zero[0]])):
            matrix[zero[0]][i] = 0
        for row in matrix:
            row[zero[1]] = 0

    print(matrix)

if __name__ == "__main__":
    matrix = [[1,2,0,5], [0, 3, 4, 6], [9, 2, 2, 7]]
    Zero(matrix)