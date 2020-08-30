#从前序和中序遍历构造二叉树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        #if not (preorder and inorder):
        if preorder ==[] or inorder == []:
            return None
		
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)

        root.left = self.buildTree(preorder[1:root_index+1],inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:],inorder[root_index+1:])
        return root