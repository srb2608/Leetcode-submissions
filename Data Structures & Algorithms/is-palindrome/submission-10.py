class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        s1=s[::-1]
        for i in range(len(s)):
            if s[i]!=s1[i]:
                return False
               
          
        return True
        
        