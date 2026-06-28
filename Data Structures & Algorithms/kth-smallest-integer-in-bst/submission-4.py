# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # arr = []
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     arr.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # arr.sort()
        # return arr[k-1]

        # arr = []
        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     arr.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        # return arr[k-1]

        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

        