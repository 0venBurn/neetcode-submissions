class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [char.lower() for char in s if char.isalnum()]

        L = 0
        R = len(filtered_chars) - 1

        while L < R:
            if filtered_chars[L] != filtered_chars[R]:
                return False
            
            L += 1
            R -= 1
        
        return True 