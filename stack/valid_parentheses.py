# Saturday March 14th 2026
#
# Problem: Valid Parentheses:
# You are given a string s made up of these bracket characters:
# '(', ')', '{', '}', '[' and ']'
#
# A string s is valid only if:
# 1. Every opening bracket is closed by the same type of closing bracket
# 2. Brackets are closed in the correct order
# 3. Every closing bracket has a matching opening bracket
#
# Return True if s is valid, and False otherwise.
#
# Thought process:
# My first idea was to use a queue. I thought I could loop through the string,
# store opening brackets, and then compare them later as I reached closing brackets.
# However, since this problem is really about checking the most recent unmatched
# opening bracket, a stack is a much better fit.
#
# I also added an early check to fail fast. If the string has an odd number of
# characters, it cannot be valid because every opening bracket must have a matching
# closing bracket.
#
# The algorithm works by using a dictionary to map each closing bracket to its
# matching opening bracket. I then loop through each character in the string.
# If the character is an opening bracket, I push it onto the stack. If it is a
# closing bracket, I check whether the top of the stack contains the matching
# opening bracket. If it does, I pop it off the stack. If not, the string is invalid.
#
# At the end, if the stack is empty, all brackets were matched correctly, so I
# return True. Otherwise, I return False because there are still unmatched
# opening brackets left in the stack.


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0