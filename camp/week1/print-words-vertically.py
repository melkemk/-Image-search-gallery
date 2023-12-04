class Solution:
    def printVertically(self, s: str) -> List[str]:
        li=list(s.split())
        print(li)
        biggest=max(len(i) for i in li)
        ans=["" for _ in range(biggest)]
        for i in range(biggest):
            for j in range(len(li)):
                if(len(li[j])<=i):
                    ans[i]+=" "
                    continue
                ans[i]+=li[j][i]
        for i in range(biggest-1,-1,-1):
            print(i)
            j=len(ans[i])-1
            while(ans[i][j]==' '):
                ans[i]=ans[i][0:-1]
                j-=1
        return ans
