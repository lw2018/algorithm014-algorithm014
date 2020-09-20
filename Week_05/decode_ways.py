#91 解码方法

class Solution:
    def numDecodings(self, s):
        #每次只能选一位或二位数字编码 相当于每次走一步或者走两步
        length = len(s)
        #dp[i] 以s[i]结尾的字符串的编码方法
        if s[0] == '0':return 0

        dp = [0]*length
        dp[0] = 1
        for i in range(1,length):
            if s[i] !='0':
                dp[i] =dp[i-1]
            value = 10 * (ord(s[i - 1]) - ord('0')) + (ord(s[i]) - ord('0'))
            if 10 <= value <= 26:
                if i == 1:
                    dp[i]+=1
                else:
                    dp[i]+=dp[i-2]
        return dp[length-1]

