#组合

class Solution:
    def combine(self, n, k):
        if k > n or k <=0 or n <=0:
            return []
        res =[]
        self.down(1,n,k,[],res)
        return res

    def down(self,start,n,K,sub_res,res):
        if len(sub_res) == K:
            res.append(sub_res[:])
            return
        
        for  v in range(start,n+1):
            sub_res.append(v)
            self.down(v+1,n,K,sub_res,res)
            sub_res.pop()