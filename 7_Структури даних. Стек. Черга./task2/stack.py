from arrayqueue import ArrayQueue
from arraystack import ArrayStack
import random


def stack_to_queue(stack):
    """
    Convert stack to queue
    """
    queue = ArrayQueue()
    while len(stack) != 0:
        num = stack.pop()
        queue.add(num)
    return queue


if __name__ == "__main__":
    queue = ArrayQueue()
    stack = ArrayStack()
    for i in range(random.randint(5, 10)):
        m = random.randint(0, 9)
        queue.add(m)
        stack.push(m)
    print('Queue: ', queue)
    print('Stack: ', stack_to_queue(stack))

