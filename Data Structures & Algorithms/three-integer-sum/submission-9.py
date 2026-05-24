class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        left = 0
        sortedNums = sorted(nums)
        res = []
        while left < len(nums):
            middle, right = left + 1, len(nums) - 1
            target = 0 - sortedNums[left]

            # skip since duplicate left pointer
            if left > 0 and sortedNums[left] == sortedNums[left - 1]: 
                left += 1
                continue

            while middle < right:
                if sortedNums[middle] + sortedNums[right] == target:
                    res.append([sortedNums[left], sortedNums[middle], sortedNums[right]])
                    middle += 1
                    right -= 1

                    while middle < right and sortedNums[middle] == sortedNums[middle - 1]:
                        middle += 1
                    
                    while middle < right and sortedNums[right] == sortedNums[right + 1]:
                        right -= 1

                elif sortedNums[middle] + sortedNums[right] < target:
                    middle += 1
                
                elif sortedNums[middle] + sortedNums[right] > target:
                    right -= 1

            left += 1
        
        return res

# [-1,0,1,2,-1,-4] becomes 
# [-4,-1,-1,0,1,2]