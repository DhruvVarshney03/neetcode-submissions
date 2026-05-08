class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s=re.sub(r'[^A-Za-z0-9]','',s)
        print(cleaned_s)
        return cleaned_s.lower()==cleaned_s[::-1].lower()
        