from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        for num in numset:
            if num-1 not in numset:
                length=1
                current=num
                while current+1 in numset:
                    current+=1
                    length+=1
                longest=max(longest,length)
        return longest
        