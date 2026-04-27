class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []

        for i in range(len(nums)):
            hashmap[nums[i]] = 1 + hashmap.get(nums[i], 0)

        while k > 0:
            max_key = max(hashmap, key=hashmap.get)
            res.append(max_key)
            max_value = hashmap.pop(max_key)
            k -= 1
        
        return res