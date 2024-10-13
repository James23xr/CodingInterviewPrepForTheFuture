# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None

        # Remove any nodes at the beginning of the list with the given val
        while head is not None and head.val == val:
            node_to_be_deleted: ListNode = head
            head = head.next
            del node_to_be_deleted

        # If the list becomes empty after removing nodes, return None
        if head is None:
            return None

        # Initialize pointers for previous and current nodes
        prev: Optional[ListNode] = head
        curr: Optional[ListNode] = head.next

        # Traverse the list and remove nodes with the given val
        while curr is not None:
            # Remove any nodes with the given val
            while curr is not None and curr.val == val:
                node_to_be_deleted = curr
                curr = curr.next
                del node_to_be_deleted

            # Update the links between nodes to bypass the removed nodes
            if prev:
                prev.next = curr
            prev = curr

            # Move to the next node
            if curr is not None:
                curr = curr.next

        # Return the modified list
        return head
        