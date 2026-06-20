class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=[]
        c=Counter(nums)
        c1 = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))
       # for i in c1:
         #   a.append(c1[i])
        c2 = list(c1.keys())
        return c2[:k]

        

        