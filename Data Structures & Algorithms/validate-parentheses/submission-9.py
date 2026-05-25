class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append('(')
            elif s[i] == '{':
                stack.append('{')
            elif s[i] == '[':
                stack.append('[')
            elif s[i] == ')':
                if len(stack) == 0 or stack[-1] != '(':
                    return False
                stack.pop()
            elif s[i] == '}':
                if len(stack) == 0 or stack[-1] != '{':
                    return False
                stack.pop()
            elif s[i] == ']':
                if len(stack) == 0 or stack[-1] != '[':
                    return False
                stack.pop()
        
        if len(stack) > 0:
            return False
        return True

# ([{}])
# push (
# push [
# push {
# see } pop {
# see ] pop [
# see ) pop (
# 
# 
# 

#(){[({})]}
# push (, pop (