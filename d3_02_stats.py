text=[12, 7, 30, 5, 18]
a=0
list=[0]
for i in text:
    for j in list:
        if text[i]<list[-j]:
            list.insert(text[i],-j)
list.remove(0)
for w in list:
    a=a+int(list[w])
    





print("最大"+list(0))
print("最小"+list(-1))
print("平均"+round(a/len(list),2))
        
        
