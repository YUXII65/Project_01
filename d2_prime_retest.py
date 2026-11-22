a=input("请输入数字：")
found=0

if a.isdigit()==False:
    print("数据错误")

    
else:
    a=int(a)
    if a<2:
        found=1

    else:
        for i in range(2,a):      
            if a%i ==0:
                found=1
                break
    if found==1:
        print("不是")
    else:
        print("是") 
