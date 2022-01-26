import numpy as np
listbg=[]
for i in range(100):
    listbg.append(a[np.random.randint(2)])
print(listbg)
leftPointer=0
righPointer=leftPointer+1
count=0
while righPointer<=len(listbg)-1:
    if listbg[leftPointer]=="G":
        leftPointer=leftPointer+1
        righPointer=leftPointer+1
    else:
        if listbg[righPointer]=="G":
            count=count+righPointer-leftPointer
            listbg[leftPointer]="G"
            listbg[righPointer]="B"
        else:
            righPointer+=1
print(count)
print(listbg)
