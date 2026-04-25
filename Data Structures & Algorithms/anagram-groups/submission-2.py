from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in strs:
            key=[0]*26
            for j in i:
                key[ord(j)-ord('a')]+=1
            dic[tuple(key)].append(i)
        return list(dic.values())


