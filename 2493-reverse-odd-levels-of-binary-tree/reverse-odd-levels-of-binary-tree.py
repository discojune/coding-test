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

                queue_left = []
                queue_right = []

                for _ in range(int(len(queue) / 2)):
                    node_1 = queue.popleft()
                    node_2 = queue.pop()

                    node_1_value = node_1.val
                    node_2_value = node_2.val

                    node_1.val = node_2_value
                    node_2.val = node_1_value

                    if node_1.left:
                        queue_left.append(node_1.left)
                        queue_left.append(node_1.right)
                    
                    if node_2.left:
                        queue_right.insert(0, node_2.left)
                        queue_right.insert(1, node_2.right)

                merge = queue_right + queue_left         
                queue = deque(merge)

            else:
                for _ in range(len(queue)):
                    node = queue.popleft()

                    if node.left:
                        queue.append(node.left)
                        queue.append(node.right)
                        
            level += 1     

        return root        

            

            



        