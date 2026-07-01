# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        result=lists[0]
        for i in range(1,len(lists)):
            result=self.mergeTwoLists(result,lists[i])
        return result
    def mergeTwoLists(self,list1,list2):
        dummy=ListNode(0)
        tail=dummy
        while list1 and list2:
            if list1.val<list2.val:
                tail.next=list1
                list1=list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail=tail.next
        if list1:
            tail.next=list1
        else:
            tail.next=list2
        return dummy.next
        