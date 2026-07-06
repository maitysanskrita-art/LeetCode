class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(index,current,total):
            if total==target:
                result.append(current[:])
                return
            if total>target or index==len(candidates):
                return
            current.append(candidates[index])
            backtrack(index,current,total+candidates[index])
            current.pop()
            backtrack(index+1,current,total)
        backtrack(0,[],0)
        return result