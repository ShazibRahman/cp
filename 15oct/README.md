#15 october (Leetcode)

1. [roman to integer](https://leetcode.com/problems/roman-to-integer/)

```python
def romanToInt( s: str) -> int:
        integer=0
        dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)-1):

            if dic[s[i]]<dic[s[i+1]]:
                integer-=dic[s[i]]

            else:
                integer+=dic[s[i]]

        integer+=dic[s[-1]]

        return integer
```


2. [integer to roman](https://leetcode.com/problems/integer-to-roman/description/)

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        roman=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        inte=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        i=0
        rom=''
        while num!=0:
          rom+=roman[i]*(num//inte[i])
          num = num % inte[i]

          i+=1
        return rom
```
