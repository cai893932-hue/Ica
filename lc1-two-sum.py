class Solution:
    # 难点：暴力穷举可能会超时，若是不知道哈希表将寸步难行
    # 思路：当使用哈希表时，对于nums[i],不需要遍历数组，只需知道是否存在y = target - nums[i]即可。
    # 复杂度：时间复杂度和空间复杂度都是 O(n)，比暴力O（n*2）简单
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            y = target - num
            if y in hash_map:
                return [hash_map[y], i]
            hash_map[num] = i
        return []
