class Solution:
    def longestPalindrome(self, s: str) -> str:
        le=len(s)
        st,end=0,0
        dp=[[False]*le for x in range(le)]
        for g in range(le):

            for  i,j in enumerate (range(g,le)):
                if g==0:
                    dp[i][j]=True
                elif g==1:
                    if (s[i]==s[j]):
                         dp[i][j]= True



                else :
                      if (s[i]==s[j]) and dp[i+1][j-1]:
                            dp[i][j]=True

                if dp[i][j]:
                    st,end=i,j

        return  s[st:end+1]
