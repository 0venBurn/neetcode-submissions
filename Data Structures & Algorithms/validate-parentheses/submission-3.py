class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"}": "{", "]": "[", ")":"("}
        stack = []

        for char in s:
            if char not in brackets:
                stack.append(char)
            if char in brackets:
                if not stack or stack[-1] != brackets[char]:
                    return False
                stack.pop()

        return True if not stack else False


        