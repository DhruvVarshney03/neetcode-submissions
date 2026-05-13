class Solution:

    def encode(self, strs: List[str]) -> str:
        str1=""
        for s in strs:
            str1+=str(s)+"1#1"
        return str1

    def decode(self, s: str) -> List[str]:
        l1=s.split("1#1")
        l1.pop()
        return l1
        
