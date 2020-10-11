#56 合并区间
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:return[]
        res =[]
        length = len(intervals)
        intervals.sort()
        left = intervals[0][0]
        right = intervals[0][1]

        for e in intervals[1:]:
            if e[0] <= right:
                if e[1] <=right:
                    pass
                if e[1]>right:
                    right=e[1]
            else:
                res.append([left,right])
                left,right=e[0],e[1]
        res.append([left,right])
        return res
