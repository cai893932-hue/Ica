class Solution:
    # 难点：通晓大小写转换和字符判断的方法，回文串的比较以及空字符串或只包含非字母数字字符的字符串的处理
    # 思路：小写用.lower(),大写用.upper()，isalnum可以进行字符判断，采用双指针法，一个一个比，且可顺便处理特殊情况
    # 复杂度：时间复杂度是O(n),遍历一次，空间复杂度是O(1)
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
