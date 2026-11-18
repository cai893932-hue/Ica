class Solution:
    #难点：若是使用双指针法，需要注意奇偶长度中心的不同
    #思路：当奇数时，中心为i；当偶数时，中心为i，i+1。
    #nonlocal是内部函数可以修改外部状态的函数，如果不用，也可以def一个state
    #复杂度：时间复杂度是O(n*2),空间复杂度是O(1)
    def countSubstrings(self, s: str) -> int:
        if not s:#提示给了s一定不是None，不过加上这一句代码更加优雅
            return 0
        count = 0
        n = len(s)
        def expand(left, right):
            nonlocal count
            while left > 0 and right < n and s[left] = s[right]:
                count += 1
                left -= 1
                right += 1
        for i in range(n):
            expand(i, i) #当奇数长度，中心为i
            expang(i,i+1) #当偶数长度，中心是i和i+1
        return count
