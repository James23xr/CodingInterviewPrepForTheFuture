# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev,cur = dummy,head
        while cur and cur.next:
            nxtpair = cur.next.next
            second = cur.next
            #swapping
            second.next = cur
            cur.next = nxtpair
            #update pointers
            prev.next = second
            prev = cur
            cur = nxtpair
        return dummy.next
        