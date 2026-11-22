a=input("输入数字：")
x=0
if a.isdigit()==False:
    print("数据异常")
else:
    a=int(a)
    if a==1:
        x=1
    else:
        for i in range(2,a):

            if a%i==0:
                x=1
                break
if x==1:
    print("不是")
else:
    print("是")
