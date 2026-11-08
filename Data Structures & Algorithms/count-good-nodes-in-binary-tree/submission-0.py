# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs approach
        #at each node, we recursively check if greater 
        #perhaps we can create an array that sotres seen at dfs
        #check if greater than max(array)
        goodNodes = 0
        pathNodes = []

        def dfs(node):
            nonlocal goodNodes
            
            if node is None:
                return 

            if not pathNodes or node.val >= max(pathNodes):
                goodNodes += 1
            pathNodes.append(node.val)
            
            dfs(node.left)
            dfs(node.right)

            pathNodes.pop() #backtrack
        
        dfs(root)

        return goodNodes


