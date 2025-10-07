# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def find_value(self, value):
            return value % 10 

    def find_rest(self, value):
        if value < 10:
            return 0

        while(value >= 10):
            value //= 10

        return value

    def push_back(self, head, value):
        newNode = ListNode(value)

        if head == None:
            return newNode
        
        current = head
        while current.next is not None:
            current = current.next

        current.next = newNode
        return head

    def addTwoNumbers(self, l1, l2):
        lResult = None
        tail = None
        rest = 0

        while l1 is not None or l2 is not None:
            valueL1 = l1.val if l1 is not None else 0
            valueL2 = l2.val if l2 is not None else 0
            lResult = self.push_back(lResult, self.find_value(valueL1 + valueL2 + rest))

            rest = self.find_rest(valueL1 + valueL2 + rest)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if rest != 0:
            lResult = self.push_back(lResult, rest)

        return lResult
            
            
        
