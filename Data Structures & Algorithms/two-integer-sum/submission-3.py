class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            required = target - nums[i]
            nums[i] = None
            if (required in nums):
                index = nums.index(required)
                return [i, index]
        