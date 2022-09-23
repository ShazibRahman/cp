flowerbed=[1,0,0,0,1]
n=2

def flow(flowerbed,n):
	le=len(flowerbed)
	if le==1:
		return True if n<=0 or flowerbed[0]==0 else False
	rem=n
	
	for i in range(le):
		if flowerbed[i]==1:
			continue
		elif (i==0 and flowerbed[i+1]==0) or (i==le-1 and flowerbed[i-1]==0) or (flowerbed[i-1]==0 and flowerbed[i+1]==0):
			flowerbed[i]=1
			rem-=1
			print(flowerbed,rem)
	return rem<=0



print(flow(flowerbed,n))
