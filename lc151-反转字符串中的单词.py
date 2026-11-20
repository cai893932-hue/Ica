class Solution:
    # 难点：如何删除空格，反转单词顺序
    # 思路：用if来条件判断，从而删除空格。在拼完单词后倒序。还有一种s.split()的解法，太优雅，可以顺手掌握
    # 复杂度：时间和空间上都是O(n)
    def reverseWords(self, s: str) -> str:
        words = []
        i, n = 0, len(s)
        while i < n:
            if s[i] == "":
                i += 1
                continue
            j = i
            while j < n and s[j] != "":
                j += 1
                words.append(s[i:j])
                i = j
        return "".join(words[::-1])
