#8. 字符串转换整数 (atoi)


class Solution:
    def myAtoi(self, s):
        s=s.strip()
        length = len(s)
        if length==0:return 0
        if s[0]=="-":
            flag =-1
        else:
            flag=1
        
        data = list(s)
        if data[0] in ["-","+"]:
            del data[0]
        res,i=0,0
        while i<len(data) and data[i].isdigit():
            res=res*10 +ord(data[i])-ord("0")
            i+=1
        return max((-2**31,min(flag*res,2**31-1)))