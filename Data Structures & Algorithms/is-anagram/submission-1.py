class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=sorted(s)
        b=sorted(t)
        if a==b:
            return True
        else:
            return False
        # m=[]
        # n=[]
        # for x in s:
        #     m.append(x)
        #     m.sort()
        # for y in t:
        #     n.append(y)
        #     n.sort()
        # if m==n:
        #     return True
        # else:
        #     return False


        