# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1=0
        sum2=0
        tens1=1
        tens2=1
        
        while l1:
            sum1+=l1.val*tens1
            tens1=tens1*10
            l1=l1.next
        while l2:
            sum2+=l2.val*tens2
            tens2=tens2*10
            l2=l2.next
        total=sum1+sum2
        if total==0:
            return ListNode(total)
        dummy=ListNode(total)
        curr=dummy
        while total!=0:
            digit=total%10
            temp=ListNode(digit)
            curr.next=temp
            curr=temp
            total=total//10
        return dummy.next

