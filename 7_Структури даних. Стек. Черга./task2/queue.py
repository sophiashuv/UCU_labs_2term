from arrayqueue import ArrayQueue
from arraystack import ArrayStack
import random

def queue_to_stack(queue):
    """
    Convert queue to stack
    """
    stack1 = ArrayStack()
    stack2 = ArrayStack()
    while len(queue) != 0:
        num = queue.pop()
        stack1.push(num)
    while len(stack1) != 0:
        num = stack1.pop()
        stack2.push(num)
    return stack2


if __name__ == '__main__':
    queue = ArrayQueue()
    stack = ArrayStack()
    for i in range(random.randint(5, 10)):
        m = random.randint(0, 10)
        queue.add(m)
        stack.push(m)
    print('Stack: ', stack)
    print('Queue: ', queue_to_stack(queue))
