class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        for i in s :
            if i in seen :
                seen[i] += 1
            else :
                seen[i]=1
        for i in t :
            if i in seen:
                seen[i]-=1
            else :
                return False 
        for c in seen.values():
            if c!=0:
                return False 
        return True

        