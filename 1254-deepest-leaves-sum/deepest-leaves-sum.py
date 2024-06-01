# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        import math

        def find_depth(x):
            n = 0
            while True:
                if x >= 2 ** n and x < 2 ** (n+1):
                    return n

                n += 1

        node_idx = 1
        visited = deque([(root, node_idx)])

        leaf_nodes = []
        depth = 0
        while visited:
            node, node_idx = visited.popleft()
            depth = find_depth(node_idx)

            if not node.left and not node.right:
                leaf_nodes.append((node.val, depth))
                continue

            if node.left:
                visited.append((node.left, 2*node_idx))

            if node.right:
                visited.append((node.right, 2*node_idx+1))

        # height = find_depth(node_idx)
        height = depth
        return sum([val for val, depth in leaf_nodes if depth == height])