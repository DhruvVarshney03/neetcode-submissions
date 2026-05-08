class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=set()
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    result.add(tuple(sorted([nums[i],nums[left],nums[right]])))
                    left += 1
                    right -= 1
                elif total<0:
                    left+=1
                elif total>0:
                    right-=1
        return list(map(list, result))