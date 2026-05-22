class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for str in strs:
            word = "".join(sorted(str))
            if word not in groups:
                groups[word] = []
            groups[word].append(str)
        return list(groups.values())


                

