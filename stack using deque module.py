from collections import deque

stack = deque()
for i in range(10000000):
    stack.append(i)

for i in range(10000000):
    stack.pop()
print(stack)
