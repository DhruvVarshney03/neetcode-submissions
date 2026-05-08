class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for index,value in enumerate(numbers):
            need=target - value 
            if need in d:
                return [d[need]+1,index+1]
                
            d[value]=index