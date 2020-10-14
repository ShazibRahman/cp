def func(ranked , player):
  out=[]
  ranked=list(set(ranked))
  ranked.sort(reverse=True)


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


