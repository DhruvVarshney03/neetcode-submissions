class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        lst=set()
        l=0
        if s=="":
            return 0
        

        for r in range(len(s)):
            
            print(lst)
            while s[r] in lst:
                lst.remove(s[l])
                l+=1
            lst.add(s[r])
            max_len=max(max_len,r-l+1)
        return max_len


