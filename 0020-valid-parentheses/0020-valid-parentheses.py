class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            # Opening brackets
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)

            # Closing brackets
            else:
                # If stack is empty
                if not stack:
                    return False

                top = stack.pop()

                # Check matching brackets
                if ch == ')' and top != '(':
                    return False
                if ch == '}' and top != '{':
                    return False
                if ch == ']' and top != '[':
                    return False

        # Stack should be empty at the end
        return len(stack) == 0