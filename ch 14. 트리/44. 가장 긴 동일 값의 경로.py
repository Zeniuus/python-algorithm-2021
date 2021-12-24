from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        visited = set()
        result = 0

        def dfs(node: Optional[TreeNode], val: int) -> int:
            nonlocal result
            if not node:
                return 0

            if node.val == val:
                visited.add(node)
                left_result = dfs(node.left, val)
                right_result = dfs(node.right, val)
                curr_result = left_result + right_result
                result = max(result, curr_result)
                return max(left_result, right_result) + 1
            else:
                dfs(node, node.val)
                return 0

        if root:
            dfs(root, root.val)

        return result
