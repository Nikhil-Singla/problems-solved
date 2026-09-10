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
            
            if not node:
                return 0, 0

            left_val, left_size = helper(node.left)
            right_val, right_size = helper(node.right)

            tot_sum, tot_size = left_val + right_val + node.val, left_size + right_size + 1

            if tot_size:
                count += int( 
                                ( (tot_sum) // (tot_size) ) == node.val
                            )
            else:
                count += 1

            return tot_sum, tot_size

        helper(root)
        return count
