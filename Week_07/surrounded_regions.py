#130. 被围绕的区域
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.n = len(board)
        if self.n == 0: return 
        self.m = len(board[0])
        
        for i in range(1,self.m-1):
            #上边
            self.dfs(board,0,i)
            #下边
            self.dfs(board,self.n-1,i)
        for i in range(self.n):
            #左边
            self.dfs(board,i,0)
            #右边
            self.dfs(board,i,self.m-1)
        for n in range(self.n):
            for m in range(self.m):
                if board[n][m] == 'f':
                    board[n][m] = 'O'
                elif board[n][m] == "O":
                    board[n][m] = 'X'
    
    def dfs(self,board,n,m):
        #终止条件
        if n < 0 or n >= self.n or m < 0 or m >= self.m or board[n][m] != 'O':
            return 
        #处理当前层
        board[n][m] = 'f'
        #递归到下一层
        self.dfs(board,n+1,m)
        self.dfs(board,n-1,m)
        self.dfs(board,n,m+1)
        self.dfs(board,n,m-1)
