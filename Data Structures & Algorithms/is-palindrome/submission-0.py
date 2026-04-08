class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.lower()
        l=0
        ns=""
        for i in s:
            if i.isalnum():
                ns+=i
        n=len(ns)
        r=n-1
        while(l<r):
            if ns[l]==ns[r]:
                l+=1
                r-=1
            else:
                return False
        return True


        