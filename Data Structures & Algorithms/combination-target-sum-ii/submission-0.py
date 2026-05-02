class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        s=[]
        candidates.sort()
        def dfs(i,total):
            if target==total:
                result.append(s.copy())
                return
            if target<total or i>=len(candidates):
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j-1]==candidates[j]:
                    continue
                s.append(candidates[j])
                dfs(j+1,candidates[j]+total)
                s.pop()
        dfs(0,0)

        return result

        