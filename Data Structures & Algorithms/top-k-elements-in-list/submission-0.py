class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict()
        d2=dict()
        res=[]
        ctr=0
        for i in range (len(nums)):
            d[nums[i]]=1+d.get(nums[i],0)
        for i in sorted(d, key=d.get, reverse=True):
            if ctr<k:
                res.append(i)
                ctr+=1
            else:
                break
        return res

            
        
    

