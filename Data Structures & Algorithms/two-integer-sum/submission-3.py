class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for ind, num in enumerate(nums):
            dict[num] = ind
        
        for i in range(len(nums)):
            y = target - nums[i]
            if y in dict and dict[y] != i:
                return [i, dict[y]]
        

            