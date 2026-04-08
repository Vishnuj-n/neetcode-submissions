class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s={}
        dic_t={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in dic_s:
                dic_s[i]+=1
            else:
                dic_s[i]=1
        
        for i in t:
            if i in dic_t:
                dic_t[i]+=1
            else:
                dic_t[i]=1
        if dic_t==dic_s:
            return True
        else:
            return False

        