# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hset = set()
        curr = head
        while curr:
            if curr in hset:
                return True
            hset.add(curr)
            curr = curr.next
        return False


        # fast, slow = head, head
        # while slow:
        #     if fast is None or fast.next is None:
        #         return False
        #     fast = fast.next.next
        #     slow = slow.next
        #     if fast == slow:
        #         return True
        
        # return False
