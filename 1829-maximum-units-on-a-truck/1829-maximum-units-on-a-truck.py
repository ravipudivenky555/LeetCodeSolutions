class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(reverse=True,key=lambda x:x[1])
        res,curr,i=0,0,0
        while curr<=truckSize:
            if i<len(boxTypes):
                if curr+boxTypes[i][0]>truckSize:
                    res+=(truckSize-curr)*boxTypes[i][1]
                    break
                curr+=boxTypes[i][0]
                res+=boxTypes[i][1]*boxTypes[i][0]
                i+=1
            else:
                break
        return res