class Solution:
    def isValid(self, s: str) -> bool:
        parens = { "}": "{", "]": "[", ")": "("}

        stack = []

        for char in s: 
            if char in parens:
                if stack and stack[-1] == parens[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
