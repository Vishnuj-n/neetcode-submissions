class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s={}
        dic_t={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            dic_s[s[i]]=dic_s.get(s[i],0)+1
            dic_t[t[i]]=dic_t.get(t[i],0)+1
        return dic_s==dic_t

        