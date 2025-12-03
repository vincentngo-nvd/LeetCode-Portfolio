from typing import Set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet: Set[str] = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            max_len = max(max_len, r - l + 1)
            
        return max_len

if __name__ == "__main__":
    solver = Solution()
    print(solver.lengthOfLongestSubstring("abcabcbb"))
    print(solver.lengthOfLongestSubstring("bbbbb"))
    print(solver.lengthOfLongestSubstring("pwwkew"))