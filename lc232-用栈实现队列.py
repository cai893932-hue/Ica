class MyQueue:
    # 难点：如何实现栈先入先出的同时，还能使得时间复杂度是O(1)
    # 思路：定义一个函数_move，使用下划线是为了表明这是个内部函数，用该函数实现摊还，从而达到O(1)的时间复杂度
    # 复杂度：空间复杂度是O(n)，存储队列中所有元素；时间复杂度是O(1)，
    def __init__(self):
        self.in_stack, self.out_stack = [], []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
