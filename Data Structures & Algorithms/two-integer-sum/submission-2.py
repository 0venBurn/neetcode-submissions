class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i, n in enumerate(nums):
            dict[n] = i
        
        for i in range(len(nums)):
            y = target - nums[i]           
            if y in dict and dict[y] != i:
                return [i, dict[y]]
            