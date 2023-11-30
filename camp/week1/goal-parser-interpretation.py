class Solution:
    def interpret(self, command: str) -> str:
        i=0
        ans=''
        while(i<len(command)):
            if(command[i]=='G'):
                ans+='G'
            elif(command[i]=='(' and command[i+1]==')' ):
                ans+='o'
                i+=1
            else:
                ans+='al'
                i+=3
            i+=1
        return ans
            