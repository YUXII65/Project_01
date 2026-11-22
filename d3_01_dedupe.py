text=[1, 2, 2, 3, 1, 4]


#不使用set

list=[]
for i in text:

    if text[i] in list:
        continue
    else:
        list.append(text[i])
print(list)        

#使用set

a=set(text)
list=[]
for i in a:
    list.append(a[i])
print(list)    
