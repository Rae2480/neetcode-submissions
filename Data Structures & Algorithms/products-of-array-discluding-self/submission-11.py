class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        totalProduct = 1
        zeroCount = nums.count(0)
        if zeroCount > 1:
            return [0] * len(nums)
        for num in nums:
            if num != 0:
                totalProduct *= num
        for i, num in enumerate(nums):
            if zeroCount == 1:
                output.append(totalProduct if num == 0 else 0)
            else:
                output.append(int(totalProduct / num))
        return output