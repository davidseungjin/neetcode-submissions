# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        1. if root is None: True
        2. not node.left and not node right OR
            not node.left and node.val < node.right.val
            not node.right and node.val > node.left.val
            node.left and node.right and node.val is between two
            recursive
        3. else: False
        '''
        # def valid(node, left, right):
        #     if not node:
        #         return True
        #     if not (left < node.val < right):
        #         return False
        #     return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        # return valid(root, float("-inf"), float("inf"))
        
        if not root:
            return True
        
        q = collections.deque([(root, float("-inf"), float("inf"))])
        while q:
            node, left, right = q.popleft()
            if not(left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))
        return True
