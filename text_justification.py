class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result=[]
        i=0
        while i<len(words):
            line_length=len(words[i])
            j=i+1
            while j<len(words) and line_length+1+len(words[j])<=maxWidth:
                line_length+=1+len(words[j])
                j+=1
            line=" "
            if j==len(words) or j-i==1:
                line=" ".join(words[i:j])
                line+=" "*(maxWidth-len(line))
            else:
                total_chars=sum(len(word) for word in words[i:j])
                total_spaces=maxWidth-total_chars
                gaps=j-i-1
                even_spaces=total_spaces//gaps
                extra_spaces=total_spaces%gaps
                for k in range(i,j-1):
                    line+=words[k]
                    line+=" "*even_spaces
                    if extra_spaces>0:
                        line+=" "
                        extra_spaces-=1
                line+=words[j-1]
            result.append(line)
            i=j
        return result


        