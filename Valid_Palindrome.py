class Solution:
    def isPalindrome(self, s: str) -> bool:

        regex = re.compile('[^a-zA-Z0-9]')
        #First parameter is the replacement, second parameter is your input string
        s = regex.sub('',s)
        s = s.lower()
        i = len(s)-1
        j=0
        k=0
        flag=False
        while j<len(s):
            if s[j]==s[i]:
                k+=1
            j+=1
            i-=1
        if k==len(s):
            return True
        else:
            return False
