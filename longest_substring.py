class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
     left=0
     charSet=set()
     maxLength=0
     for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left+=1
        charSet.add(s[right])
        maxLength=max(maxLength,right-left+1)
     return maxLength