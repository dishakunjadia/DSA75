# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):

        if not root : return 0

        q = deque([root])
        answer = 1
        level = 1 
        max_sum = float('-inf')

        while q:
            level_sum = 0
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                answer = level
            level += 1 
        return answer
            
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        