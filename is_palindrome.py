# LeetCode 9. 回文数  难度：简单
# 难点：负数和以 0 结尾的非零数都不是回文，需要提前排除
# 思路：反转一半数字——每次取 x 的末位拼到 rev 上，当 rev >= x 时停下，
#       偶数位比较 x == rev，奇数位比较 x == rev // 10
# 复杂度：时间 O(log10 x)（数字位数），空间 O(1)
def is_palindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10


if __name__ == "__main__":
    tests = [(121, True), (-121, False), (10, False), (0, True), (12321, True)]
    for n, want in tests:
        got = is_palindrome(n)
        assert got == want, f"is_palindrome({n}) = {got}, want {want}"
    print("All tests passed!")
