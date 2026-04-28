class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for idx, num in enumerate(nums):
            indices[num] = idx
        print(indices)
        
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in indices and indices[diff] != idx:
                if indices[diff] < idx:
                    return [indices[diff], idx]
                else:
                    return [idx, indices[diff]]








