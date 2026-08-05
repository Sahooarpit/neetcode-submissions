class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()

        l= r = 0
        ans = 0

        n = len(s)
        while r != n:

            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l +=1
            seen.add(s[r])
            r += 1

            ans = max(r-l, ans)

        return ans
        

