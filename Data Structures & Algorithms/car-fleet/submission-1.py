class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count=0
        a=[]
        for i in range(len(speed)):
            a.append((position[i],(target-position[i])/speed[i]))
        a.sort(reverse=True)
        max_time=0
        for i,j in a:
            # for j in range(i+1,len(a)):
            #     if position[i]<position[j] and a[i]<=a[j]:
            #         count-=1    
            if  j>max_time:
                max_time=j
                count+=1
        return count
