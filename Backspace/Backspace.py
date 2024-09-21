line = list(input())

stack = []
for char in line:
    stack.append(char)
    if(char=="<"):
        stack.pop()
        stack.pop()

print("".join(stack))
