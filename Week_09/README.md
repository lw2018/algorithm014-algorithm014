学习笔记
最长子序列 最长子串的问题 dp[i]可定义为以s[i]结尾的最长子序列/子串的XX

不同路径2的状态转移方程
```
#有障碍时 无论从上还是从下都无法到达障碍所在的格子 因为要绕开障碍
if obstacleGrid[n][m]==1:
        dp[n][m]=0
else:
    dp[n][m] = dp[n][m-1]+dp[n-1][m]
```