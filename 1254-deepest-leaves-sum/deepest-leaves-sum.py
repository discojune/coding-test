# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque

        queue = deque([root])

        while queue:
            leave_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                
                leave_sum += node.val
            
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return leave_sum