# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        curr_sum = 0

        def reverse_dst(node: TreeNode):
            nonlocal curr_sum
            if node.right:
                reverse_dst(node.right)
            node.val += curr_sum
            curr_sum = node.val
            if node.left:
                reverse_dst(node.left)

        reverse_dst(root)
        return root
