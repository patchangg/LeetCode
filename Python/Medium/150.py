
def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token not in "+-/*":
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left+right)
            elif token == "-":
                stack.append(left-right)
            elif token == "*":
                stack.append(left*right)
            else:
                stack.append(int(float(left)/right))
    return stack.pop()

# Go through the tokens, if a number appears, put it into the stack.
# If an expression appears, pop the last two numbers in the stack and evaluate
# them in the reverse order and append the result back into the stack.
# O(n), O(n) space
tokens = ["2","1","+","3","*"]
value = evalRPN(tokens)
print(value)
