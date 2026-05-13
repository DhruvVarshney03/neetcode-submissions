class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=set()
        for i in range (len(nums)):
            for j in range (len(nums)):
                if (nums[i]+nums[j]==target) and (i!=j):
                    ans.add(i)
                    ans.add(j)
                    break
                else:
                    pass
        return list(ans)