#493. 翻转对

#先统计 再marge
class Solution:
    def reversePairs(self, nums):
        return self.mergeSort(nums, 0, len(nums)-1)
       
    def mergeSort(self, nums, l, r):
        if l >= r:return 0
        mid = l + ((r - l) >> 1)
        count =self.mergeSort(nums,l,mid) + self.mergeSort(nums,mid+1,r)
        i, j=l, mid+1
        while i<=mid:
            while j<=r and nums[i] > 2*nums[j]:
                j+=1
            count= count +j -(mid+1)
            i+=1
        self.merge(nums, l, mid, r)
        return count

    def merge(self, nums, left, mid, right):
        temp = []
        i = left
        j = mid+1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i +=1
            else:
                temp.append(nums[j])
                j +=1
        while i<=mid:
            temp.append(nums[i])
            i +=1
        while j<=right:
            temp.append(nums[j])
            j +=1
        nums[left:right+1] = temp
