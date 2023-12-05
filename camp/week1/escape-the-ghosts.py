class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        minimum=inf
        for ghost in ghosts:
            local=0
            g=ghost
            while(g[0]!=target[0]):
                if(g[0]>target[0]):
                    g[0]-=1
                else:
                    g[0]+=1
                local+=1
            while(g[1]!=target[1]):
                if(g[1]>target[1]):
                    g[1]-=1
                else:
                    g[1]+=1
                local+=1
            minimum=min(minimum,local)
        g=[0,0]
        local=0
        while(g[0]!=target[0]):
            if(g[0]>target[0]):
                g[0]-=1
            else:
                g[0]+=1
            local+=1
        while(g[1]!=target[1]):
            if(g[1]>target[1]):
                g[1]-=1
            else:
                g[1]+=1
            local+=1
        return local<minimum