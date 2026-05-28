class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max = float('-inf')
        count = 0
        # Example [1, 1, 0, 1, 1, 1]

        # Memory num = 0
        # variable count = 0
        # curr_max = 2

        for num in nums:  
            if num == 1: 
                count += 1 
                curr_max = max(curr_max, count)
            else:
                count = 0
                curr_max = max(curr_max, count)

        curr_max = max(curr_max, count)

        return curr_max
                


            





        