def splitjoin(text,arg):
 arr = []
 string = str()
 for m in range(0,len(text)):
  if not text[m] in forbidden:
   arr.append(text[m])
  if text[m] in forbidden:
   arr.append(" ")
 for n in range(0,len(arr)):
  if n < len(arr)-1:
   if not (arr[n] == " " and arr[n+1] == " "):
    string += arr[n]
  if n == len(arr)-1:
   string += arr[n]
 if arg == 0:
  return arr
 else: return string 
