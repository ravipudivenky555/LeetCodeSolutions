class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=y=0
        for i in moves.lower():
            if i=='u':x-=1
            elif i=='d':x+=1
            elif i=='r':y+=1
            elif i=='l':y-=1
        return x==y==0