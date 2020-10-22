class Solution:
    def isSubsequence(self, s: str, t: str) :
        i,j,le1,le2=0,0,len(s),len(t)
        while i< le1 and j<le2:
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                j+=1
        return le1==i
