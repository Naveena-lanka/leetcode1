class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        
        n = len(s) // 2
        m = len(s)

        for i in range(n):
            if s[i] != s[m-1-i]:
                return False

        return True
