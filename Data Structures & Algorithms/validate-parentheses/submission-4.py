class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for e in s:
            if e in hmap:
                if not stack or stack[-1] != hmap[e]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(e)
        return len(stack) == 0
        # stack = []
        # for e in s:
        #     if e in hmap:
        #         if not stack or (stack and stack[-1] != hmap[e]):
        #             return False
        #         else:
        #             stack.pop()
        #     else:
        #         stack.append(e)
        # return len(stack) == 0