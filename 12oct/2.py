class MinStack:

    def __init__(self):
        self.st=[]
        self.minimun=None

        """
        initialize your data structure here.
        """


    def push(self, x: int) -> None:
        self.st.append(x)
        self.minimun=min(self.st) if self.st else None


    def pop(self) -> None:
        self.st.pop()
        self.minimun=min(self.st) if self.st else None


    def top(self) -> int:
         return self.st[-1]


    def getMin(self) -> int:
        return self.minimun
