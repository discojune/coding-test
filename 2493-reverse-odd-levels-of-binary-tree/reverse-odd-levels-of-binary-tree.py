# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import deque

        level = 0
        queue = deque([root])

        while queue:
   
            if level % 2 != 0:
                for i in range(int(len(queue) / 2)):
                    node_1 = queue[i]
                    node_2 = queue[len(queue)-1-i]

                    node_1_value = node_1.val
                    node_2_value = node_2.val

                    node_1.val = node_2_value
                    node_2.val = node_1_value

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)
                        
            level += 1     

        return root        

            

            



        