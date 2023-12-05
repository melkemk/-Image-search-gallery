class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp=list(s)
        for i,j in enumerate(s):
            temp[indices[i]]=j
        return  ''.join(map(str, temp))
