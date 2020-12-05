def minMax(a,b):
 min = a[0]
 max = a[0]
 indx = int()
 for k in range(0,len(a)):
  if min > a[k]:
   min = a[k]
   indx = k
  if min <= a[k]:
   min = min
  if max < a[k]:
   max = a[k]
  if max >= a[k]:
   max = max
 if b == 0:
  return min
 if b == 1:
  return max
 if b == 2:
  return indx 
