# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        stack = []

        while(fast.next.next != None):
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        stack.append(slow.val)
        slow = slow.next
        ret = 0
        
        while stack:
            ret = max(ret, stack.pop() + slow.val)
            slow = slow.next

        return ret
