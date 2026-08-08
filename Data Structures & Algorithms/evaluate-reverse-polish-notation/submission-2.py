class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == "+":
                stack.append(stack.pop() + stack.pop())
            elif ch == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            elif ch == "*":
                stack.append(stack.pop() * stack.pop())
            elif ch == "/":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(ch)) # must return int
        return stack[0]