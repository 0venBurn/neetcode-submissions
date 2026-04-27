class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for idx, num in enumerate(nums): 
            subtraction = target - num
            if subtraction in hashmap:
                return [hashmap[subtraction], idx]
            hashmap[num] = idx
        
        for num in hashmap: 
            subtraction = target - num
            if subtraction in hashmap:
                if hashmap[num] != hashmap[subtraction]:
                    return sorted([hashmap[num], hashmap[subtraction]])