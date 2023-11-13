from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = l1.val
        number2 = l2.val
        counter = 1
        next_node = l1.next
        while next_node is not None:
            number1 += next_node.val * pow(10, counter)
            next_node = next_node.next
            counter += 1

        next_node = l2.next
        counter = 1
        while next_node is not None:
            number2 += next_node.val * pow(10, counter)
            next_node = next_node.next
            counter += 1

        list_sum_number = [int(x) for x in str(number1 + number2)]

        result = ListNode()
        if len(list_sum_number) == 0:
            return result
        elif len(list_sum_number) == 1:
            result.val = list_sum_number[0]
            return result
        else:
            result.val = list_sum_number.pop()
            result.next = ListNode()
            next_item = result.next
            for index in range(len(list_sum_number) - 1, 0, -1):
                next_item.val = list_sum_number[index]
                next_item.next = ListNode()
                next_item = next_item.next
            next_item.val = list_sum_number[0]

        return result
