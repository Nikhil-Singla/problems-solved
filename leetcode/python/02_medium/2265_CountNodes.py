# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0

        def helper(node):
            nonlocal count
            
            if node.left != None:
                left_val, left_size = helper(node.left)
            else:
                left_val, left_size = 0, 0

            if node.right:
                right_val, right_size = helper(node.right)
            else:
                right_val, right_size = 0, 0

            if (left_size + right_size):
                average = (left_val + right_val + node.val) // (left_size + right_size + 1)
            else:
                average = node.val

            if node.val == average:
                count += 1

            return (left_val + right_val + node.val), (left_size + right_size + 1 ) 

        helper(root)
        return count
