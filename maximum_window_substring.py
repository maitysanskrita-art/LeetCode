class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need={}
        for ch in t:
            need[ch]=need.get(ch,0)+1
        have={}
        required=len(need)
        formed=0
        left=0
        min_len=float('inf')
        start=0
        for right in range(len(s)):
            ch=s[right]
            have[ch]=have.get(ch,0)+1
            if ch in need and have[ch]==need[ch]:
                formed+=1
            while formed==required:
                if right-left+1<min_len:
                    min_len=right-left+1
                    start=left
                have[s[left]]-=1
                if s[left] in need and have[s[left]]<need[s[left]]:
                    formed-=1
                left+=1
        if min_len==float('inf'):
            return ""
        return s[start:start+min_len]
        