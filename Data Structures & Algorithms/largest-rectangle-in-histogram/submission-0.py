class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        i=0
        while i<len(heights):
            left=right=i
            while left>0 and heights[i]<=heights[left-1]:
                left-=1
            while right<len(heights)-1 and heights[i]<=heights[right+1]:
                right+=1
            area= heights[i]*(right-left+1)
            max_area= max(max_area,area)
            i+=1
        return max_area