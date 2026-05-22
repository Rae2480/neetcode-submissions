class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            count = [0] * 26  
            for char in word:
                count[ord(char) - ord('a')] += 1  

            # make count immutable to make it hashable
            count = tuple(count) 

            if count not in groups:
                groups[count] = []
            
            groups[count].append(word)
        
        return list(groups.values())
            
