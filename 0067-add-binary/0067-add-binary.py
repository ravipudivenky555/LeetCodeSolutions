class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans=list()
        m=len(a)-1
        n=len(b)-1
        carry=0
        while m>=0 and n>=0:
            j=int(a[m])
            k=int(b[n])
            ans.insert(0,((j+k+carry)%2))
            carry=(j+k+carry)//2
            m-=1
            n-=1
        while m>=0:
            j=int(a[m])
            ans.insert(0,((j+carry)%2))
            carry=(j+carry)//2
            m-=1
        while n>=0:
            j=int(b[n])
            ans.insert(0,((j+carry)%2))
            carry=(j+carry)//2
            n-=1
        ans.insert(0,carry)
        ansstr=""
        for i in range(len(ans)):
            if i==0 and ans[i]==0:
                continue
            ansstr=ansstr+str(ans[i])
        return ansstr