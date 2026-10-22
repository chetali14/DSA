class Solution(object):
    def calculate(self, s):
        stack = []
        result = 0
        num = 0
        sign = 1

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)

            elif c == '+':
                result += sign * num
                num = 0
                sign = 1

            elif c == '-':
                result += sign * num
                num = 0
                sign = -1

            elif c == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif c == ')':
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()

        return result + sign * num