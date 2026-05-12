class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list=[]
        for i in range (len(nums)-(k-1)):
            #print(nums[i:i+k])
            max_element=max(nums[i:i+k])
            max_list.append(max_element)
        print(max_list)
        return max_list