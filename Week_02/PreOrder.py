#--coding:--utf-8--
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res=[]
        
    def preorderTraversal(self, root):
        
        if root:
            self.res.append(root.val)
            if root.left:
                self.preorderTraversal(root.left)
            if root.right:
                self.preorderTraversal(root.right)
        return self.res