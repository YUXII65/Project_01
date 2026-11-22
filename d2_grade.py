for i in range(5):
    s=input("请输入第"+str(i+1)+"个人的成绩：")
    
    if s==-1:
            print("缺考")
            continue

    if s.isdigit()==False:
        continue

    else:
        s=int(s)
        
        if s>100 or s<0:
            print("数据异常")
            continue
        elif s>=90:
            level="A"
        elif s>=80:
            level="B"
        elif s>=60:
            level="C"
        else:
            level="D"
        print("分数"+str(s)+" → 等级"+level)
