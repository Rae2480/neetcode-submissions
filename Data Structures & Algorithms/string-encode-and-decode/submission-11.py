class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for string in strs:
            output.append(str(len(string)))
            output.append(",")
            output.append(string)
        return "".join(output)
        # 2,hi5,hello

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ",":   
                j += 1
            prefix = int(s[i:j])
            start = j+1
            word = s[start:start+prefix]
            output.append(word)
            i = start + prefix
        return output

        

