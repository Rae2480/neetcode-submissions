class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for num in nums: 
            if num not in numbers:
                numbers[num] = 0
            numbers[num] += 1
        freq = sorted(numbers.items(), key=lambda x: x[1], reverse=True)
        output = []
        for i in range(k):
            output.append(freq[i][0])
        return output
            