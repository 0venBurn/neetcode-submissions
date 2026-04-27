class Solution:
    def isValid(self, s: str) -> bool:
        # check if its a opening or closing bracket
        brackets = {"]": "[", "}": "{", "]": "[", ")": "("}
        stack = []

        for char in s:
            if char in brackets:
                if not stack or stack[-1] != brackets[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return True if not stack else False          

        