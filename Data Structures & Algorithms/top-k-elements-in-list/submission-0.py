class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for num in nums:
            if num not in freq:
                freq[num] = 0
            
            freq[num] += 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            ans.append(sorted_freq[i][0])
        
        return ans

            