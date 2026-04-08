class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_=0
        start=0
        dic={}
        for end in range(len(s)):
            dic[s[end]]=dic.get(s[end],0)+1
            
            while dic[s[end]]>1:
                dic[s[start]]-=1
                start+=1
            max_ = max(max_,end-start+1)
        return max_
        