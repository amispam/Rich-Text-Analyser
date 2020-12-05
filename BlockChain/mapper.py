def mapper(p,q):
 map = []
 for m in range(0,len(p)):
  for n in range(0,len(p)):
   if p[m] == q[n]:
    map.append(n)
 return map
