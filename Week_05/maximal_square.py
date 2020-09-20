
#221 最大正方形
def maximalSquare(atrix):
    if not matrix or len(matrix[0])==0:return 0
    row = len(matrix)+1
    col = len(matrix[0])+1
    dp = [[0]*col for _ in range(row)]
    maxSize = 0
    for r in range(row-1):
        for c in range(col-1):
            if matrix[r][c] =='1':
                dp[r+1][c+1] = min(dp[r][c],dp[r+1][c],dp[r][c+1]) +1
                maxSize = max(maxSize,dp[r+1][c+1])
    return maxSize*maxSize
