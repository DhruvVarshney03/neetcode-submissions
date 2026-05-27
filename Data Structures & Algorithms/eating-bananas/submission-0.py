class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right=max(piles)
        left=1
        result=right
        while left<=right:
            k=(left+right)//2
            hours=0

            for pile in piles:
                hours+=(pile+k-1)//k

            if hours<=h:
                result=k
                right=k-1
            else:
                left=k+1
        
        return result
            