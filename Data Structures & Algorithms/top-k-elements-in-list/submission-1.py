class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        n=len(nums)
        freq=[[] for i in range(n+1)]
        for i in nums:
            dic[i]=1+dic.get(i,0)
        for num,count in dic.items():
            freq[count].append(num)
        result=[]
        for inner_list in reversed(freq):
            for j in inner_list:
                result.append(j)
                if len(result)==k:
                    return result


        
