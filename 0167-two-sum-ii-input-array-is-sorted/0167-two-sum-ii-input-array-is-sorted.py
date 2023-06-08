class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ind1=0;ind2=len(numbers)-1
        while ind1<ind2:
            sumCheck=numbers[ind1]+numbers[ind2]
            if sumCheck==target:break
            elif sumCheck<target:ind1+=1
            else:ind2-=1
        return [ind1+1,ind2+1]