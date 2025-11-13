"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ptr1 = p
        ptr2 = q
        while ptr1!=ptr2:
           ptr1 = ptr1.parent if ptr1.parent else p
           ptr2 = ptr2.parent if ptr2.parent else q
        return ptr1
        