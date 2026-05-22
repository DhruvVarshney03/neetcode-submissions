class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # max_area=0
        # i=0
        # while i<len(heights):
        #     left=right=i
        #     while left>0 and heights[i]<=heights[left-1]:
        #         left-=1
        #     while right<len(heights)-1 and heights[i]<=heights[right+1]:
        #         right+=1
        #     area= heights[i]*(right-left+1)
        #     max_area= max(max_area,area)
        #     i+=1
        # return max_area

        stack=[]
        max_area=0

        for i, h in enumerate(heights):
            start=i

            while stack and stack[-1][1]>h:
                index, height= stack.pop()

                area= height*(i-index)
                max_area=max(max_area, area)
                start=index

            stack.append((start,h))

        for index, height in stack:
            area= height*(len(heights)-index)
            max_area=max(max_area, area)
        
        return max_area