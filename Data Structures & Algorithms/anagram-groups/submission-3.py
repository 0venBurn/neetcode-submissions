class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord("a") - ord(char)] += 1
            values[tuple(count)].append(string)
        
        return values.values()

        