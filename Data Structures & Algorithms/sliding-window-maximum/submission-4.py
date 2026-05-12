class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # max_list=[]
        # for i in range (len(nums)-(k-1)):
        #     #print(nums[i:i+k])
        #     max_element=max(nums[i:i+k])
        #     max_list.append(max_element)
        # #print(max_list)
        # return max_list
        N = len(nums)

        queue = deque()
        i = 0
        while i < k:
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            i += 1
        result = [max(nums[: k])]
        i, j = 0, k
        while j < N:

            if queue and queue[0] == nums[i]:
                queue.popleft()
            while queue and queue[-1] < nums[j]:
                queue.pop()
            queue.append(nums[j])
            if queue:
                result.append(queue[0])
            i += 1
            j += 1
        return result
            
            
                
