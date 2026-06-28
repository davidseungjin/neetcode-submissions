# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # if not head:
        #     return
        
        # node = []
        # curr = head
        # while curr:
        #     node.append(curr)
        #     curr = curr.next
        
        # i, j = 0, len(node) - 1
        # while i < j:
        #     node[i].next = node[j]
        #     i += 1
        #     if i >= j:
        #         break
        #     node[j].next = node[i]
        #     j -= 1
        # node[i].next = None

        '''
        1. find the middle of the linked list using slow and fast
        2. reverse the second half of the list
        3. merge the two linked list one by one
        '''
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow points to the end of the first half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        


