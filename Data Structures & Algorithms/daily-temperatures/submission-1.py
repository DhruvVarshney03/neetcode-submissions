class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res=[0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i,len(temperatures)):
        #         if temperatures[i]<temperatures[j]:
        #             res[i]=j-i
        #             break
        # return res

        n = len(temperatures)
        result = [0] * n
        stack = []   
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result