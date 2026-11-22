# W1D5 · ② 抄  手打示例（15 分钟）
# 任务卡 §五 里有一段 7 行代码，把它手打到这里。
# 要求：不看键盘，逐行打；每打完 2 行按一次 F5。
# 打完先别改，直接运行，看到 891 和一行字典再往下走。
import csv
with open("data/titanic.csv",encoding="utf-8",newline="")as f:
    reader=csv.DictReader(f)
    rows=list(reader)
print(len(rows))

for k in rows[0].keys():
    print(k)
for i in range(5):
    print(rows[i]["survived"] + " " + rows[i]["sex"] + " " + rows[i]["fare"])


#1.准备一个计数器count，从0开始
#2.遍历rows里的每一行
#3.如果这一行的age等于空字符串，count加1
#4.循环结束后，打印count

def count_empty(rows,col):
    count=0
    for row in rows:
        if row[col]=="":
            count=count+1
    return count       

print(count_empty(rows,"age"))
print(count_empty(rows,"deck"))






counts={}
sums={}
for row in rows:
    k=row["pclass"]
    if k in counts:
        counts[k]+=1
    else:
        counts[k]=1
    if k in sums:
      sums[k]+=float(row["fare"])
    else:
        sums[k]=float(row["fare"])

for k in counts:
    print(k+","+str(counts[k])+","+str(sums[k]))
    print(str(sums[k] / counts[k]))    
