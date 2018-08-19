class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = ['a']
        
        for c in s:
            if c in ['(','{','[']:
                stack.append(c)
            else:
                if (c == ')' and stack[-1] == '('):
                    stack.pop()
                elif (c == '}' and stack[-1] == '{'):
                    stack.pop()
                elif (c == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    stack.append(c)

                
        if stack[-1] == 'a':
            return True
        else:
            return False
