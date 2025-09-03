# Author: Dylan Spence

'''
https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1
Parenthesis Checker:
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']', verify the validity of the arrangement.
An input string is valid if:

         1. Open brackets must be closed by the same type of brackets.
         2. Open brackets must be closed in the correct order.
'''

class Solution:
    def isBalanced(self, s):
        stack = []
        for c in s:
            match c:
                case '(':
                    stack.append(c)
                case ')':
                    if len(stack) == 0:
                        return False
                    if stack[len(stack)-1] != '(':
                        return False
                    stack.pop()
                case '{':
                    stack.append(c)
                case '}':
                    if len(stack) == 0:
                        return False
                    if stack[len(stack)-1] != '{':
                        return False
                    stack.pop()
                case '[':
                    stack.append(c)
                case ']':
                    if len(stack) == 0:
                        return False
                    if stack[len(stack)-1] != '[':
                        return False
                    stack.pop()
        
        if len(stack) != 0:
            return False
        
        return True


test = Solution()
s = "[()()]{}"
print(test.isBalanced(s))