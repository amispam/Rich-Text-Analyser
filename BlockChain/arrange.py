def arrange(p,y,index):
 domain = []
 codomain = []
 for k in range(0,len(p)):
  for i in range(k,len(p)):
   if p[k] < p[i]:
    p = swap(p,k,i)
    domain.append(k)
    codomain.append(i)
 for z in range(0,len(domain)):
  y = swap(y,domain[z],codomain[z])
 if index == 0:
  return p
 else:
  return y
