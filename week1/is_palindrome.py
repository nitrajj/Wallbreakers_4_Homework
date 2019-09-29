import re

def isPalindrome(self, s: str) -> bool:
    s = re.sub("[^A-Za-z0-9]","",s).lower()
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True

    l = 0
    r = len(s)-1
    while l < r:
        print(s[l])
        print(s[r])
        if s[l] == s[r]:
            l+=1
            r-=1
        else:
            return False
    
    return True

str1 = "A man, a plan, a canal: Panama"
isPalindrome(str1)