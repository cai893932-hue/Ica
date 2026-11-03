class Solution:
    # 难点: 简单
    # 思路：第一个是标准写法，也可以用while；第二个是评论区爆火的消消乐玩法
    # 复杂度：O(n)

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

    def isValids(self, s: str) -> bool:
        while "{}" in s or "()" in s or "[]" in s:
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            s = s.replace("()", "")
        return s == ""
