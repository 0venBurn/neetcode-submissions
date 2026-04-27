class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s = Counter(s)
        count_t = Counter(t)

        for i in count_s:
            if count_s[i] != count_t.get(i, 0):
                return False
        
        return True
        
        
        