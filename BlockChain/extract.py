def extract(arg):
 if not (arg[len(arg)-1] == ","):
  arg+=","
 i = int()
 j = int()
 data = []
 while i < len(arg):
  if arg[i] == ",":
   try:
    data.append(float(arg[j:i]))
    j = i+1
   except:
    print("Error...")
    break
  if i == len(arg)-1:
   i = 0
   break
  i+=1
 return data
