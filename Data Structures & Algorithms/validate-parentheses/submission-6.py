class Solution:
    def isValid(self, s: str) -> bool:
        a=[]       
        d={']':'[','}':'{',')':'('}
        for c in s:
            if c in d:
                if a and a[-1] == d[c]:
                    a.pop()
                else:
                    return False
            else:
                a.append(c)
        return not a
