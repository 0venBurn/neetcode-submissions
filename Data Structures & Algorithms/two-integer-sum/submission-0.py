class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(len(nums)):
            dict[nums[i]] = i
        
        for i in range(len(nums)):
            y = target - nums[i]
            if y in dict and dict[y] != i:
                return [i, dict[y]]