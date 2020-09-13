class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        i=0
        j=i+1
        x = 0
        y = 0
        l = len(A)
        for i in range(l):
            if A[i]<= A[j]:
                x = x+1
            if A[i]>= A[j]:
                y = y+1
            i+=1
        if x==(l-1) or y ==(l-1):
            return(True)
        return(False)
