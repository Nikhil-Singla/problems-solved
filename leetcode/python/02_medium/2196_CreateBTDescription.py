# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for x, y, left in descriptions:
            if x not in nodes:
                nodes[x] = TreeNode(x)
            if y not in nodes:
                nodes[y] = TreeNode(y)
            if left:
                nodes[x].left = nodes[y]
            else:
                nodes[x].right = nodes[y]
            
            children.add(y)

        for x, y, z in descriptions:
            if x not in children:
                return nodes[x]

        return None