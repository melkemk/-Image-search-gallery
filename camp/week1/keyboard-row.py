class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"
        ans=[]
        for x in words:
            word=x.lower()
            can_be_written=True
            for each_word in word:
                if(each_word not  in row1):
                    can_be_written=False
            # print(can_be_written)
            if(can_be_written):
                ans.append(x)
                continue
            can_be_written=True
            for each_word in word:
                if(each_word not  in row2):
                    can_be_written=False
            if( can_be_written):
                ans.append(x)
                continue
            can_be_written=True
            for each_word in word:
                if(each_word not  in row3):
                    can_be_written=False
            if( can_be_written):
                ans.append(x)
                continue
        return ans