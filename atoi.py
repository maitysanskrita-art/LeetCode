class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.lstrip()
        if not s:
            return 0
        sign=1
        index=0
        if s[index]=='-':
            sign=-1
            index+=1
        elif s[index]=='+':
            index+=1
        num=0
        while index<len(s) and s[index].isdigit():
            digit=int(s[index])
            num=num*10+digit
            index+=1
        num*=sign
        int_min=-2**31
        int_max=2**31-1
        if num<int_min:
            return int_min
        if num>int_max:
            return int_max
        return num    
        