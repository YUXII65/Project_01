text=[3, 1, 3, 2, 3, 1]
a={}
for i in text:
    a[i]=a.get(i,0)+1
list=[]
for j in a:
    list.append(a[j])
list.sort()
print(list[-1])
