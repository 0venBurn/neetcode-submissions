class Solution:
    nums = [1, 1, 2, 3]
    target = 2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices:
                return sorted([indices[diff], i])
            indices[n] = i
        
        return []


