class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        matrix_sums = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    matrix_sums[row][col] = matrix[row][col]
                elif row == 0:
                    matrix_sums[row][col] = matrix[row][col] + matrix_sums[row][col-1]
                elif col == 0:
                    matrix_sums[row][col] = matrix[row][col] + matrix_sums[row-1][col]
                else:
                    matrix_sums[row][col] = matrix[row][col] \
                    + (matrix_sums[row][col-1]) \
                    + (matrix_sums[row-1][col]) \
                    - (matrix_sums[row-1][col-1])
        ans = 0
        for y1 in range(m):
            for y2 in range(y1, m):
                subarray_sums = defaultdict(int)
                subarray_sums[0] = 1
                for x in range(n):
                    matrix_sum = matrix_sums[y2][x]
                    if y1 > 0:
                        matrix_sum -= matrix_sums[y1-1][x]
                    if matrix_sum - target in subarray_sums:
                        ans += subarray_sums[matrix_sum - target]
                    subarray_sums[matrix_sum] += 1
        return ans