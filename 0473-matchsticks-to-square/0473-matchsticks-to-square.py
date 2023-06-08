class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4 : return False
        numSum = sum(nums)
        nums.sort(reverse=True)
        if numSum % 4 != 0: return False
        target = [numSum/4] * 3
        if nums[0]>numSum/4: return False
        counts = dict()
        for i in nums:
            counts[i]=counts.get(i,0)+1
        def dfs(counts, target,maxs,truemax,k,inits=False):
            if k-1 > 0:
                if inits:
                    for x, y in counts.items():
                        if y != 0:
                            target[0]-=x
                            counts[x]-=1
                            if dfs(counts,target,x+1,truemax,k,False):
                                return True
                            target[0]+=x
                            counts[x]+=1
                            return False
                if target[0]==0:
                    return dfs(counts,target[1:],truemax,truemax,k-1,True)
                for x, y in counts.items():
                    if x <=target[0] and y>0 and x< maxs:
                        target[0]-=x
                        counts[x]-=1
                        if dfs(counts,target,x+1,truemax,k):
                            return True
                        target[0]+=x
                        counts[x]+=1
                if target[0]!=0:
                    return False
            return True
        return dfs(counts, target,nums[0]+1,nums[0]+1,4,inits=True)