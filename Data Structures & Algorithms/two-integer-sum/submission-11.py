class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in indices:
                return sorted([indices[diff], i])
            indices[n] = i
        return []


