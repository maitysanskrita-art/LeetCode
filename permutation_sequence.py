class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers=[]
        factorial=1
        answer=""
        for i in range(1,n+1):
            numbers.append(str(i))
        for i in range(1,n):
            factorial*=i
        k-=1
        while numbers:
            index=k//factorial
            answer+=numbers[index]
            numbers.pop(index)
            if not numbers:
                break
            k%=factorial
            factorial//=len(numbers)
        return answer