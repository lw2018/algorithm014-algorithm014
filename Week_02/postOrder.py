class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postorderTraversal(self, root):
        
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.res.append(root.val)
        return self.res