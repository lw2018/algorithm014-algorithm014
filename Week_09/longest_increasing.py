#300 最长上升子序列

class Solution:
    def lengthOfLIS(self, nums):
          #dp[i]  以s[i]结尾的最长上升子序列
        length= len(nums)
        dp =[1]*length
        for i in range(length):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] =max(dp[i],dp[j]+1)
        res=0
        for i in dp:
            res=max(res,i)
        return res
