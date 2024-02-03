# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        # 연결 리스트가 홀수 개로 연결되어 있는 경우, 중앙을 한번 더 이동한다.
        if fast:
            slow = slow.next
            
        # 팰린드롬 여부 확인
        # slow 런너는 중앙값으로부터 끝까지 나아가면서 rev와 값을 비교하며 팰린드폼인지를 확인한다.
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next # 각 러너의 포인트를 이동한다.

        return not rev

