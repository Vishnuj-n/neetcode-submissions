class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length=0
        start=0
        state={}
        current_max=0
        for end in range(len(s)):
            state[s[end]] = state.get(s[end],0)+1
            current_max=max(current_max,state[s[end]])
            if current_max+k<end-start+1:
                state[s[start]]-=1
                start+=1
            max_length = max(max_length,end - start + 1)
        return max_length
            
            
            

        