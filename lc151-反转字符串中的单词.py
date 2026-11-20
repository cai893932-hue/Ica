class Solution:
    # 难点：跳过首尾/中间多余空格，只反转单词顺序而不反转单词内部字符
    # 思路：i 跳过空格定位单词开头，j 向后找到空格确定结尾，切出整词收集到 words，最后倒序拼接。
    #       （更简便的是 return " ".join(s.split()[::-1])：split() 自带按空白切分并丢弃空串）
    # 复杂度：时间 O(n)，空间 O(n)（words 存所有单词）
    def reverseWords(self, s: str) -> str:
        words = []
        i, n = 0, len(s)
        while i < n:
            if s[i] == " ":                 # 跳过空格（写成 "" 空串永远不成立）
                i += 1
                continue
            j = i
            while j < n and s[j] != " ":    # 走到单词结尾
                j += 1
            words.append(s[i:j])            # 整词只收集一次；放内层会切成单字符碎片
            i = j
        return " ".join(words[::-1])        # 词间补回单个空格
