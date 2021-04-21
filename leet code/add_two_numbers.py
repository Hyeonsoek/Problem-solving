# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def listNodeToInt(self, l1 : ListNode): 
        ret = []
        while l1 != None:
            ret.insert(0, str(l1.val))
            l1 = l1.next
        ret = int(''.join(ret))
        
        return ret
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        integer1 = self.listNodeToInt(l1)
        integer2 = self.listNodeToInt(l2)
        
        target = list(str(integer1 + integer2))
        
        targetNode = None
        for x in target:
            if targetNode:
                targetNode = ListNode(int(x), targetNode)
            else:
                targetNode = ListNode(int(x))
        return targetNode
        
        