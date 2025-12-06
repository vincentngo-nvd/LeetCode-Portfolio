#Python/String/0003_LongestSubstringWithoutRepeatingCharacters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            
        return max_len

if __name__ == "__main__":
    solver = Solution()
    print(solver.lengthOfLongestSubstring("abcabcbb"))
    print(solver.lengthOfLongestSubstring("bbbbbb"))
    print(solver.lengthOfLongestSubstring("pwwkew"))