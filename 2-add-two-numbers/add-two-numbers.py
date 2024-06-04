from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10

            current.next = ListNode(new_digit)
            current = current.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy_head.next

# Helper function to create linked list from list of numbers
def create_linked_list(numbers):
    dummy_head = ListNode(0)
    current = dummy_head
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return dummy_head.next

# Helper function to convert linked list to list of numbers
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
