class Solution:
    # 难点：base case 要先定住（n<=2 直接返回 n），否则递归/递推都推不动；
    #       另外注意递归版不记 memo 是指数级，会超时。
    # 思路：到第 n 层只有两种来法 —— 从 n-1 层爬 1 步，或从 n-2 层爬 2 步，
    #       所以 f(n) = f(n-1) + f(n-2)。递推只需滚动的两个变量。
    # 复杂度：递推 时间 O(n) / 空间 O(1)；朴素递归 时间 O(2^n) / 空间 O(n)（对照用）
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev, curr = 1, 2          # f(1), f(2)
        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr
        return curr
