class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix=[[0]*n]*m
        for i in range(m):
            for j in range(n):
                if (i==0 or  j==0):
                    matrix[i][j]=1
                else :
                    matrix[i][j]=matrix[i][j-1]+matrix[i-1][j]

        return matrix[m-1][n-1]
