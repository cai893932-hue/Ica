class Solution:
    # 难点：一是 middle 的求法，left + (right - left) // 2 是 C/Java 的防溢出写法
    #       （Python 整数不会溢出，(left + right) // 2 也能用，这么写是为了看懂别人的代码）；
    #       二是边界必须成套：区间怎么定义，决定了 right 的初始值、while 条件、right 的更新方式，
    #       三处混着写就会死循环或者漏掉答案。
    # 思路：数组有序且无重复元素 -> 想到二分。像 0~100 猜数字，每次砍掉一半，所以快。
    # 复杂度：时间 O(log n)，空间 O(1)

    def search(self, nums: list[int], target: int) -> int:
        """写法一：target 可能存在的区间是左闭右闭 [left, right]。"""
        left, right = 0, len(nums) - 1
        while left <= right:                  # 区间里还有元素时继续
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1             # middle 已排除，从右边一格开始
            else:
                right = middle - 1            # middle 已排除，到左边一格结束
        return -1

    def search_right_open(self, nums: list[int], target: int) -> int:
        """写法二：区间是左闭右开 [left, right)，三处配套差异都在注释里。"""
        left, right = 0, len(nums)            # 差异1：right 取 len(nums)，不是 len(nums) - 1
        while left < right:                   # 差异2：[left, left) 是空区间，所以用 <
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1             # middle 已排除
            else:
                right = middle                # 差异3：middle 本身在区间外，无需 -1
        return -1
