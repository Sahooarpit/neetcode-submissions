class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0

        words = {}
        currMax = 0
        ans = 0

        for i in range(len(s)):
            words[s[i]] = 1 + words.get(s[i], 0)

            currMax = max(currMax, words[s[i]])

            while(i-l+1) - currMax > k:

                words[s[l]] -= 1
                l += 1
            
            ans = max(ans, i-l+1)     
        return ans