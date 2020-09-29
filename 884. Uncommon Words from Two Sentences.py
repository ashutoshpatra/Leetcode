class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        d={}
        for w in A.split():
            if w in d:
                d[w]=d.get(w,0)+1
            else:
                d[w]=1
        for w in B.split():
            if w in d:
                d[w]=d.get(w,0)+1
            else:
                d[w]=1
        unmatchedW=[w for w in d if d[w]==1]
        return unmatchedW
