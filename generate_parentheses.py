class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtrack(current,open_account,close_account):
            if len(current)==2*n:
                result.append(current)
                return
            if open_account<n:
                backtrack(current+"(",open_account+1,close_account)
            if close_account<open_account:
                backtrack(current+")",open_account,close_account+1)
        backtrack("",0,0)
        return result
        