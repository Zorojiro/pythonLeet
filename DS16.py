# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root, res):
            if not root:
                return 0
            
            right = height(root.right, res)
            left = height(root.left, res)

            res[0] = max(res[0], right+left)

            return 1 + max(right, left)

        res = [0]
        height(root, res)
        return res[0]

        