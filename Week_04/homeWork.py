#第4周homework

# 860 柠檬水找零
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveCount,tenCount = 0,0
        length = len(bills)
        for i in bills:
            if i == 5:
                fiveCount+=1
            elif i == 10:
                fiveCount -= 1
                if fiveCount >= 0:
                    tenCount += 1
                else:
                    return False
            elif i == 20:
                tenCount -=1
                fiveCount -=1
                if tenCount >=0 and fiveCount>=0:
                    pass
                elif fiveCount -2 >= 0:
                    pass
                    tenCount += 1
                    fiveCount -= 2
                else:
                    return False    
        return  True

# 买卖股票的最佳时机 II
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length < 2:
            return 0
        dp = [[0]*2 for _ in range(length)]

        #第一天卖出状态的最大利润
        dp[0][0] = 0
        #第一天买入状态的最大利润
        dp[0][1] = -prices[0]
        for i in range(1,length):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        #最后最大利润一定是卖出状态
        return dp[length-1][0]

#分发饼干
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_len = len(g)
        s_len = len(s)
        g_index = 0
        s_index =0
        count=0

        if g_len ==0 or s_len ==0: return 0
        while g_index <g_len and s_index < s_len:
            if s[s_index] >= g[g_index]:
                count +=1
                s_index +=1
                g_index +=1
            else:
                s_index +=1
        return count


# 200. 岛屿数量
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.length = len(grid)
        if self.length ==0:
            return 0
        self.sub_length = len(grid[0])
        self.count = 0
        for y in range(self.length):
            for x in range(self.sub_length):
                if grid[y][x] =="1":
                    n=self.dfs(grid,y,x)
                    self.count = self.count+n
        return self.count


    def dfs(self,grid,y,x):
        if  self.inArea(grid,y,x) == False:
            return 0
        if grid[y][x] != "1":
            return 0
        grid[y][x] = "2"
        #self.count +1
        self.dfs(grid,y-1,x)
        self.dfs(grid,y+1,x)
        self.dfs(grid,y,x-1)
        self.dfs(grid,y,x+1)
        return 1


    def inArea(self,grid,y,x,):
        return x >=0 and y >=0 and y < self.length and x < self.sub_length


#153. 寻找旋转排序数组中的最小值
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1
        start, end = 0, len(nums)-1
        while start <= end:
            half = (start+end) // 2
            if nums[half] >= nums[0]: 
                start = half+1
            elif nums[half] <= nums[len(nums)-1]:
                end = half-1
        if start == len(nums):
            return nums[0]
        else:
            return nums[start]

#