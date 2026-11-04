class Solution:
    # 难点：遇到右括号时栈可能是空的，必须先判空再 pop（否则 IndexError）；
    #       右括号要反查左括号，用 dict 映射比一串 if 干净。
    # 思路：isValid 用栈 —— 遇左压栈，遇右与栈顶比对，最后栈空才算合法；
    #       isValid_reduce 是「消消乐」写法 —— 反复替换掉相邻成对括号，看能否删空。
    # 复杂度：isValid 时间 O(n) / 空间 O(n)；
    #         isValid_reduce 最坏 O(n^2)（每轮 replace 都要重扫整串，层数可达 n/2）。

    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False

        return not stack

    def isValid_reduce(self, s: str) -> bool:
        while "{}" in s or "()" in s or "[]" in s:
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            s = s.replace("()", "")
        return s == ""
