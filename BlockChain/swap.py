def swap(p,i,j):
 q = []
 for z in range(0,len(p)):
  q.append(p[z])
 q[i] = p[j]
 q[j] = p[i]
 return q
