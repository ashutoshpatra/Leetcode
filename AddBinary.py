class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a.zfill(max(len(a),len(b)))
        b = b.zfill(max(len(a),len(b)))
        i=len(a)-1
        c=0
        total=[]
        while i>=0:
            x = len(total)-1
            if len(total) == 0:
                x=0
            s = int(a[i])+int(b[i])+c
            if s==3:
                total[:0] = [1]
                c=1
            
            elif s==2:
                total[:0] = [0]
                c=1
            else:
                total[:0] = [s]
                c=0
            i-=1
            x-=1
        if c!=0:
            total[:0] = [c]
        total = ''.join(map(str, total))
        return total
