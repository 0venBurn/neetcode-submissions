class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        count = 0

        for num in nums: 
            if num != 1: 
                result = max(count, result)
                count = 0 
            else:
                count += 1
            
        return max(count, result)


                


            





        