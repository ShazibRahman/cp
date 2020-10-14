def func(ranked , player):
  out=[]
  ranked=list(set(ranked))
  ranked.sort(reverse=True)
  print(ranked)

  i=0
  while i < len(player):
     while ranked and ranked[-1]<= player[i]:
       ranked.pop()

     if not ranked:
        out.append(1)
     else:
        out.append(len(ranked)+1)
     i+=1

  return out



print(func([100 ,100 ,50 ,40 ,40 ,20 ,10],[5 ,25 ,50 ,120]))

def fu(a):
  while a:
    if a[-1]==a[-2]:
      a.pop()
