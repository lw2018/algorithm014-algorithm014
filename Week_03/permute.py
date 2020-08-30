#全排列

class Solution:
    def permute(self, nums) :
        #self.nums=nums
        res=[]
        lenth = len(nums)
        self.down(0,res,lenth,nums)
        return res


    def down(self,first,res,lenth,nums):
        if first==lenth:
            res.append(nums[:])

        for i in range(first,lenth):
            nums[first], nums[i] = nums[i], nums[first]
            self.down(first+1,res,lenth,nums)
            nums[first], nums[i] = nums[i], nums[first]