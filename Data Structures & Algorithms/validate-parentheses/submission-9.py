class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack to determine and check if its a balanced bracket or not 
        brackets = {"]": "[", "}": "{", ")":"("}
        stack = []

        for char in s:
            if char in brackets:
                if not stack or stack[-1] != brackets[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)

        return True if not stack else False        

        