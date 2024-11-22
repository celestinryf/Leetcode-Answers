class Solution:
    def isValid(self, s: str) -> bool:
        # Hard coded solution

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''


        # Optimal solution using a stack

        stack = []
        # Initiate a HashMap with keys (closing bracket), and values (opening bracket)
        closeToOpen = {')' : '(', ']' : '[', '}' : '{'}

        for c in s:
            if c in closeToOpen:
                # stack[-1] represents the top of the stack, or the most recently viewed element
                if stack and stack[-1] == closeToOpen[c]: # c is a key, passed into the Map returns a value
                    stack.pop() # remove the top (opening bracket), and don't add the closing
                else:
                    return False
            else:
                stack.append(c)
        # If all elements have found their partner the stack must be empty
        return True if not stack else False