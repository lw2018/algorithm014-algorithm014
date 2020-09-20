#363 矩形区域不超过 K 的最大数值和

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        row = len(matrix)
        col = len(matrix[0])
        res = float('-inf')
        for r in range(col):
            rowSum = [0] * row
            for c in range(r,col):
                for r in range(row):
                    rowSum[r] = rowSum[r] + matrix[r][c]

                temp = [0]
                subSum = 0
                for e in rowSum:
                    subSum = subSum + e
                    left = bisect.bisect_left(temp, subSum - k)
                    if left < len(temp):
                        res = max(subSum - temp[left],res)
                    bisect.insort(temp, subSum)
            if res == k:
                return res
        return res