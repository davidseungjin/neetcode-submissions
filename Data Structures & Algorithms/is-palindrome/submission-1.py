class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        1. i, j and 
        2. iterate and check 
        2-1. if i is not alphanumeric, continue and i++
        2-2. if j is not alphanumeric, continue and j--
        2-3. if i != j, return False
        3. return True
        '''

        i = 0
        j = len(s) -1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True