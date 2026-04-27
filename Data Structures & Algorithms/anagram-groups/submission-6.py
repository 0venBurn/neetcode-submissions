class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = defaultdict(list)

        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char) - ord("a")] += 1
            keys[tuple(arr)].append(word)
        
        return keys.values()