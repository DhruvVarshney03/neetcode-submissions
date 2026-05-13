class Solution:
    def isValid(self, s: str) -> bool:
        # if len(s)==1:
        #     return False
        
        brackets={'}':'{', ']':'[', ')':'('}
        stack=[]
        for bracket in s:
            if bracket in brackets.values():
                stack.append(bracket)
            

            if bracket in brackets.keys():
                if not stack:
                    return False
                if stack[-1]!=brackets[bracket]:
                    return False
            
                stack.pop()
                    
        return not stack
            
          