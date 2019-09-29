class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            print(26*result)
            result = (26*result + ord(s[i])-64)
        return result
        
        
        