def finder(txt,argument,argumentPrime):
 global glob1
 global glob2
 global glob3
 global glob4
 arr = []
 arr1 = []
 occurance = []
 word = []
 j = 0
 m = 0
 for i in range(0,len(txt)):
  if txt[i] == " ":
   arr.append(txt[j:i])
   j = i+1
 for k in range(0,len(arr)):
  s = 0
  m = 0
  for m in range(0,len(arr)):
   if arr[k] == arr[m]:
    s+=1
  occurance.append(s)
  word.append(arr[k])
 out = []
 for ma in range(1,len(arr)):
  na = 0
  while na < ma and ma < len(arr):
   if arr[na] == arr[ma]:
    out.append(ma)
    na=ma
   if not arr[na] == arr[ma]:
    na+=1
 grandList = []
 grandIndex = []
 global arrangeGrandIndex 
 for last in range(0,len(arr)):
  if not (last in out):
   grandList.append(arr[last])
   grandIndex.append(occurance[last])
 arrangeGrandIndex = arrange(grandIndex,grandList,0)
 arrangeGrandList = arrange(grandIndex,grandList,1)
 if argumentPrime == 0:
  print("There are {0} word/words with repetition, and {1} word/words without repetition, further analysis (from highest to lowest occurance order) is given below".format(len(arr),len(arrangeGrandList)))
 if argument == "rCount" and argumentPrime==0:
  for analysis in range(0,len(arrangeGrandList)):
   print("[{0}] repeated {1} time/times".format(arrangeGrandList[analysis],arrangeGrandIndex[analysis]))
 if argument == "iPosition" or argumentPrime==0:
  for grandListIndex in range(0,len(grandList)):
   print("["+grandList[grandListIndex]+"] found at index:")
   arrIndex = 0
   storaData = []
   while arrIndex < len(arr) and grandListIndex < len(grandList):
    if arr[arrIndex] == grandList[grandListIndex]:
     storaData.append(arrIndex+1)
    arrIndex += 1
   print(storaData)
 for percentage in range(1,101):
  glob1.append((len(arrangeGrandIndex)*percentage)/100)
  glob3.append(percentage)
 percentageCount = 0
 for percentageCount in range(0,100):
  bookNewPlace = 0
  percentageNew = 0
  while percentageNew <= glob1[percentageCount]-1 and percentageCount < 100:
   bookNewPlace += arrangeGrandIndex[percentageNew]
   percentageNew += 1
  bookNewPlace = ((bookNewPlace/len(arr))*100)
  glob2.append(bookNewPlace)
 for glob2Index in range(0,len(glob2)):
  if glob2Index == 0:
   glob4.append(glob2[0])
  else: glob4.append(glob2[glob2Index]-glob2[glob2Index-1])

 if argument == "none":
  return 
