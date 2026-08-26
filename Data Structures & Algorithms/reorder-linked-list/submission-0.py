# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # find and save second half head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next

        # split list and reverse second half
        prev = slow.next = None
        while second_head:
            save = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = save
        
        # merge two halfs
        first, second = head, prev

        # second is either same length as first or shorter if the total  list is uneven
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        


