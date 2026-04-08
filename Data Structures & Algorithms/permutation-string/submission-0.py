class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start=0
        state={}
        k=len(s1)
        sf=Counter(s1)

        for end in range(len(s2)):
            state[s2[end]]=state.get(s2[end],0)+1
            if end-start+1==k:
                if state==sf:
                    return True
                state[s2[start]]-=1
                if state[s2[start]]==0:
                    del state[s2[start]]
                start+=1
        
        return False
                

        