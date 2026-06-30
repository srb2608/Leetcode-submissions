class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        l1=0
        for a in nums:
            if a-1 not in nums:
                l=1
                while a+l in nums:
                    l+=1
                l1=max(l1,l)
        return l1
                

      

        
        