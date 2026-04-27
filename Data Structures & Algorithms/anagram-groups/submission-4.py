class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = defaultdict(list)

        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord("a") - ord(char)] += 1
            values[tuple(key)].append(string)
        return values.values()

        