class Solution:
    def busyStudent(self, a: List[int], b: List[int], c: int) -> int:
        i=0
        while a and b:
            if c>=a[-1] and c<=b[-1]:

                i+=1
            a.pop()
            b.pop()
        return i
