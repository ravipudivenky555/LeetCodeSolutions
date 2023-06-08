class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        tops = []
        for e in envelopes:
            if tops and tops[-1][0] < e[0] and tops[-1][1] < e[1]: 
                tops.append(e)
                continue
            for i in range(len(tops)):
                if tops[i][1] >= e[1]: 
                    tops[i] = e
                    break
            else:
                tops.append(e)
        return len(tops)