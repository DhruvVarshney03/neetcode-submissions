class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashMap={}
        for num in nums:
            hashMap[num]=hashMap.get(num,0)+1
            if hashMap[num]>1:
                return num