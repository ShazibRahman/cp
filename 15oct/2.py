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
