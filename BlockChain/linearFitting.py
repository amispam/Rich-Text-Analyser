def interpolate(p,q):
 rslt = []
 angle = []
 intersept = []
 i1 = float()
 j1 = (-pi/2)+0.1
 k1 = int()
 if not (len(p) == len(q)):
  print("Error... data should only occur in (x,y) pair format")
 yBar = int()
 xBar = int()
 for k in range(0,len(q)):
  yBar += q[k]
  xBar += p[k]
 yBar = yBar/len(q)
 xBar = xBar/len(q)
 while j1 < (pi/2)-0.1:
  for k2 in range(0,len(p)):
   if k2+1 == len(p):
    angle.append(tan(j1))
    intersept.append(yBar-(xBar*tan(j1)))
   i1+=abs(line(tan(j1),p[k2],yBar-(xBar*tan(j1)))-q[k2])
  rslt.append(i1)
  i1 = 0
  j1+=0.01
 print("Average repetition line is :\ny = ({0})x+({1})".format(angle[minMax(rslt,2)],intersept[minMax(rslt,2)]))
 # line 1 points 
 s1 = x
 t1 = []
 for kp1 in range(0,len(x)):
  t1.append(line(angle[minMax(rslt,2)],x[kp1],intersept[minMax(rslt,2)]))
 fig = plt.figure()
 plt.subplot(2,1,1)
 plt.plot(s1, t1,linewidth=2, label = "average repetition")
 plt.plot(x, y, label= "repetition", color= "red",linestyle="dashed",linewidth=1,marker= ".",markerfacecolor="green", markersize=5)   
 plt.xlabel('word index from highest repetition to lowest repetition') 
 plt.ylabel('repetition count of word') 
 plt.title('Analysis of data!') 
 plt.legend()
 plt.subplot(2,1,2)
 plt.plot(glob3,glob2,label="% graph", color="purple", linestyle="dashed", linewidth=1, marker="o", markerfacecolor="blue",markersize=5)
 plt.xlabel("top x% of the words")
 plt.ylabel("y% of the total word count")
 plt.grid()
 plt.legend()
 fig.add_subplot(3,3,2)
 plt.plot(glob3,glob4,label=" s", color="brown", linestyle="dashed", linewidth=1, marker="*", markerfacecolor="brown",markersize=5)
 plt.xlabel("x% of the words")
 plt.ylabel("y% of the total word count")
 plt.grid()
 plt.legend()
 plt.show()
