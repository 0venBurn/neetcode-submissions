class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)

        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord("a") - ord(char)] += 1 
            
            mapping[tuple(key)].append(string)
        
        return mapping.values()
        