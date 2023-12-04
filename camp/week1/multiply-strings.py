class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        t=1
        ans=0
        for i in range(len(num1)-1,-1,-1):
            # for j in range(len(num2)-1,0,-1):
            ans+=t*int(num2)*int(num1[i])
            t*=10
        return str(ans)

