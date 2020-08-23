#--coding:--utf-8--

class Solution:
    def twoSum(self, nums, target):
        length =  len(nums)
        numsDict = {}
        for  i in  range(0,length):
            another = target - nums[i]
            if another in numsDict:
                return [numsDict[another],i]
            numsDict[nums[i]] = i