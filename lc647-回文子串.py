class Solution:
    #难点：奇偶长度的中心不同；左端点必须用 left >= 0，否则 s[0] 处的中心/回文不会被计数
    #思路：枚举每个中心向两侧扩展。奇数长度中心为 i；偶数长度中心为 i, i+1。
    #      每成功匹配一次 count += 1，恰好对应"以该中心的最长扩展"中的每一层回文
    #nonlocal 是声明而非函数：让内层 expand 绑定到外层的 count，赋值改的是外层变量
    #      而不是新建局部变量；不用它也可以改成 expand 返回本中心的回文数再累加
    #复杂度：时间 O(n²)（n 个中心 × 每次 O(n) 扩展），空间 O(1)
    def countSubstrings(self, s: str) -> int:
        if not s:  # 提示给了 s 一定非空，不过加上这一句代码更加优雅
            return 0
        count = 0
        n = len(s)
        def expand(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        for i in range(n):
            expand(i, i)      # 奇数长度，中心为 i
            expand(i, i + 1)  # 偶数长度，中心是 i 和 i+1
        return count
