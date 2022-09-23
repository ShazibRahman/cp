class Solution:
    def plusOne(self, a: List[int]) -> List[int]:
        b=[]
        carry,f=0,0
        while a:

            if f==0 :
                b.insert(0,((a[-1]+1)%10))
                carry=(a.pop()+1)//10
                f+=1
            else:
                b.insert(0,(a[-1]+carry)%10)
                carry=(a.pop()+carry)//10

        if  carry:
            b.insert(0,carry)
        return b
