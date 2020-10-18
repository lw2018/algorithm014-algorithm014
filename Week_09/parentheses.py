#32. 最长有效括号

class Solution:
    def longestValidParentheses(self, s):
        # 0到i部分的最大有效括号的长度 且这个最大有效括号以s[i]结尾
        length = len(s)
        dp =[0]*length
        res =0
        for i in range(1,length):
            #以右括号结尾
            if s[i] == ")":
                if s[i-1]=="(":
                    if i>=2:
                        dp[i] =dp[i-2]+2
                    else:
                        dp[i] =2
                elif (i-dp[i-1]-1)>=0 and s[i-dp[i-1]-1]=="(":
                    if (i-dp[i-1]-2)>=0:
                        dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2]
                    else:
                        dp[i] =dp[i-1]+2
                else:
                    dp[i]=0
                res= max(res,dp[i])
        return res