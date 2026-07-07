class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        result=[0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                digit1=ord(num1[i])-ord('0')
                digit2=ord(num2[j])-ord('0')
                product=digit1*digit2
                position1=i+j
                position2=i+j+1
                total=product+result[position2]
                result[position2]=total%10
                result[position1]+=total//10
        answer=""
        for digit in result:
            if not (answer==""and digit==0):
                answer+=str(digit)
        return answer
        