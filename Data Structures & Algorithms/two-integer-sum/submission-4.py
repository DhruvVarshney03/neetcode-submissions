class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i!=j) and (nums[i]+nums[j]==target):
                    ans.add(i)
                    ans.add(j)
        return list(ans)    

            