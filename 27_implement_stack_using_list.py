# Stack is LIFO
# Last In First Out

stack = []

def push_(x):
    stack.append(x)
    print(x, "pushed")

def pop_():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        return stack.pop()

def peek_():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        return stack[-1]

def isempty_():
    return len(stack) == 0

def size_():
    return len(stack)
