class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # hashMap={}
        # for num in nums:
        #     hashMap[num]=hashMap.get(num,0)+1
        #     if hashMap[num]>1:
        #         return num
        slow=nums[0]
        fast=nums[0]

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break

        slow=nums[0]

        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        
        return slow