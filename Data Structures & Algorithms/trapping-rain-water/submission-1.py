class Solution:
    def trap(self, height: List[int]) -> int:
        # trappedWater=0
        # i=0
        # for x in range(0,len(height)):
        #     if height[x]>0:
        #         i=x
        #         break
        # for j in range(i+1, len(height)):
        #     if height[j]==0:
        #         continue
        #     width=j-i-1
        #     if width>0:
        #         trappedWater+= min(height[j], height[i])*(width)
        #         i=j
        # stack1 = []
        # for i in range(len(height)):
        #     stack1.append(stack1[-1] if stack1 and stack1[-1] > height[i] else height[i])
        
        # stack2 = []
        # for i in range(len(height) - 1, -1, -1):
        #     stack2.append(stack2[-1] if stack2 and stack2[-1] > height[i] else height[i])
        # stack2 = stack2[::-1]

        # result = 0
        # for i in range(len(height)):
        #     result += max(0, min(stack1[i], stack2[i]) - height[i])
        # return result

        if not height:
            return 0

        l, r =0, len(height)-1
        leftMax, rightMax=height[l], height[r]
        res=0
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax=max(leftMax, height[l])
                res+=leftMax-height[l]
            else:
                r-=1
                rightMax=max(rightMax, height[r])
                res+=rightMax-height[r]
        return res

                