# Python3
class Solution:
    def minDepth(self, root):
        # Define the depth-first search
        def dfs(root):
            if root is None:
                return 0
            # If only one of child is non-null, then go into that recursion.
            if root.left is None:
                return 1 + dfs(root.right)
            elif root.right is None:
                return 1 + dfs(root.left)
            # Both children are non-null, hence call for both children.
            return 1 + min(dfs(root.left), dfs(root.right))

        return dfs(root)