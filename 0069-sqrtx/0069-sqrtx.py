class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1 or x==0:
            return x
        n=1
        mylist=list()
        while (n*n)<=x:
            mylist.append(n)
            n+=1
        l,h=0,len(mylist)-1
        ans=1
        while l<=h:
            mid=(l+h)//2
            if mylist[mid]**2==x:
                return mylist[mid]
            elif mylist[mid]**2<x:
                ans=mylist[mid]
                l=mid+1
            elif mylist[mid]**2>x:
                h=mid-1
        return int(ans)