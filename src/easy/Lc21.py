# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        listResult = None

        while(list1 is not None or list2 is not None):
            value, which = self.takeMinValue(list1, list2)
            listResult = self.pushBack(listResult, value)

            if which == 1:
                list1 = list1.next if list1 else None
            else:
                list2 = list2.next if list2 else None
    
        return listResult
    
    def takeMinValue(self, list1, list2):
        if list2 is None:
            return list1.val, 1
        elif list1 is None:
            return list2.val, 2

        return (list1.val, 1) if list1.val <= list2.val else (list2.val, 2)

    def pushBack(self, head, value):
        newNode = ListNode(value)
        if head is None:
            return newNode

        current = head
        while current.next is not None:
            current = current.next
        current.next = newNode
        return head
