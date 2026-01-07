# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):

        MOD = 10**9 + 7
        self.max_product = 0

        # 1st DFS: compute total sum
        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        total = total_sum(root)

        # 2nd DFS: compute subtree sums & max product
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            sub_sum = node.val + left + right
            product = sub_sum * (total - sub_sum)
            self.max_product = max(self.max_product, product)

            return sub_sum
        dfs(root)
        return self.max_product % MOD
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        