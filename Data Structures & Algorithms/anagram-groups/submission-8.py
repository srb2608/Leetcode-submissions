class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c=[False]*len(strs)
        b=[]
        for x in range(len(strs)):
            a=[strs[x]] 
            if c[x]==True:
                continue
            else:
                c[x]=True           
            for y in range(x+1, len(strs)):
                if c[y]==True:
                    continue
                if sorted(strs[x]) == sorted(strs[y]):
                    a.append(strs[y])
                    c[y]=True
            b.append(a)
        return b
           


        
