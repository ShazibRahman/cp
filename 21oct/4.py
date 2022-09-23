class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        max_=0
        for i in range(len(s)):
            if s[i]=="(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    max_=max(max_,i-st[-1])
        return max_
