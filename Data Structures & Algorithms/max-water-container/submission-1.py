class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        #right= len(heights)-1
        for left in range(len(heights)):
            for right in range(left,len(heights)):
                area= min(heights[left], heights[right])*(right-left)
                max_area= max(area, max_area)
        return max_area
    
    

    