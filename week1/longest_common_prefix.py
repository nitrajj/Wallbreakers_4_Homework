import re

def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs: 
        return ""
    if len(strs) == 1: 
        return strs[0]
    
    prefix = strs[0]
    
    for i in range(1, len(strs)):
        match = re.match(prefix,strs[i])
        while not match:
            prefix = prefix[:-1]
            match = re.match(prefix,strs[i])
        
    return prefix

strs = ["flower","flow","flight"]

longestCommonPrefix(strs)