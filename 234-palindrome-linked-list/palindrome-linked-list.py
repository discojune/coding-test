# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q_head: Deque = collections.deque()

        if not head:
            return True

        node = head

        while node is not None:
            q_head.append(node.val)
            node = node.next

        while len(q_head) > 1:
            if q_head.popleft() != q_head.pop():
                return False

        return True

            

