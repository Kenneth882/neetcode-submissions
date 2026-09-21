# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Inital approach. get the lenght of the list by traversing and counting. One i have the count do len-n+1 then find the elements from the top
        lst_len=0
        curr=head
        while curr:
            lst_len+=1
            curr=curr.next
        front=lst_len-n
        if front==0:
            return head.next
        curr2=head
        val=0
        while curr2:
            if val+1==front:
                curr2.next=curr2.next.next
                
                break
            else:
                curr2=curr2.next
                val+=1
        return head
