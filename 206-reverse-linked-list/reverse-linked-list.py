# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev

            next, node.next = node.next, prev # head의 끝 값을 향해가는 next라는 새로운 ListNode, 이전 값을 백트래킹하는 prev를 설정

            return reverse(next, node)

        return reverse(head)



        
        
        