# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = [list1.val]
        while list1.next is not None:
            result.append(list1.val)
            list1 = list1.next
        result.append(list2.val)
        while list2.next is not None:
            result.append(list2.val)
            list2 = list2.next
        result.sort()
        new_result = ListNode()
        current = ListNode()
        for index in range(len(result)-1, -1, -1):
            current.val = result[index]
            new_result.next = current
            current = new_result
        return new_result