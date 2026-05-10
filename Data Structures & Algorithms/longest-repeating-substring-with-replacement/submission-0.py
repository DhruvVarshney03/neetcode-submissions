class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # freq=Counter(s)
        # print(freq)
        # most_char=max(freq, key=freq.get)
        # print(most_char)

        max_len=0
        unique_chars=set(s)
        
        for most_char in unique_chars:
            left=0
            replacement=0
            for right in range(len(s)):
                if s[right]!=most_char:
                        replacement+=1
                
                while replacement>k:
                    if s[left]!=most_char:
                        replacement-=1
                    left+=1
                max_len=max(max_len, right-left+1)
                

        return max_len




            

