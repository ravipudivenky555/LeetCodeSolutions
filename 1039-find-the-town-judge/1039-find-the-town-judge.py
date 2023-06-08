class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0 and n==1:
            return 1
        if len(trust)==0:
            return -1
        personList=[]
        trustList=dict()
        res=-1
        for i,_  in trust:
            if i in personList:
                continue
            personList.append(i)
        if len(personList)==n:
            return -1
        personList.sort()
        if personList[-1]==n-1:
            res=n
        i=0
        while i<len(personList):
            if personList[i]!=i+1:
                res=i+1
                break
            i+=1
        if res==-1:
            return -1
        for _,j in trust:
            if j in trustList:
                trustList[j]+=1
            else:
                trustList[j]=1
        if trustList[res]==n-1:
            return res
        else:
            return -1