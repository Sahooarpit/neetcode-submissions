class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i))
            res += "#"
            res += i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        lastEnd = 0
        
        while len(s) != 0:

            ind = 0

            while s[ind] != "#":
                ind += 1
            
            print(s[:ind])
            length = int(s[:ind])
            res.append(s[ind+1:ind+1+length])
            s = s[ind + length+1:]

        return res

