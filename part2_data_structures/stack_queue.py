stack = []
queue = []

def push(val):
    stack.append(val)
def pop():
    return stack.pop()

def enqueue(val):
    queue.append(val)
def dequeue():
    return queue.pop(0)