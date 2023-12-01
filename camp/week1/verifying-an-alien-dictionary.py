class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        largest=max(len(i) for i in words)
        for j in range(len(words)-1):
                minimum=min(len(words[j]),len(words[j+1]))
                for i in range(minimum):
                    if((order.index(words[j][i])>(order.index(words[j+1][i])))):
                        return False       
                    if((order.index(words[j][i])<(order.index(words[j+1][i])))):
                        if i==minimum-1 and  len(words[j])> len(words[j+1]):
                            return True
                        break
                if i==minimum-1:                  
                    if  len(words[j])> len(words[j+1]):
                        return False
        return True