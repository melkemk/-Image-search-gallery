class Solution:
    def largestGoodInteger(self, num: str) -> str:
        j=0
        ar=[" "]
        ze=0
        for i in num:
            if(i==0):
                ze+=1
            if(i!=ar[j][0]):
                ar.append(i)
                j+=1
            else:
                if( not len(ar[j])==3):
                    ar[j]+=i
        ar.pop(0)
        print(ar)
        arr=[i for i in ar if len(i)==3]
        print(arr)
        if(len(arr)==0):
            return ""
        x=str(max(list(map(int,arr))))
        if(x=='0'):
            return "0"*3
        return x
