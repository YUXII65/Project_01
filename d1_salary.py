# d1_salary.py
# W1D1 抄写练习 · 2026-11-16
# 工资计算器 v0.1
# 今天只用到：变量 / str / float / print / input / 类型转换 / 注释

name = input("请输入姓名：")
hourly = input("请输入时薪（元）：")
hours = input("请输入本月工时：")
bonus=input("请输入本月奖金：")
tax_rate=input("请输入税率（小数）：")
hourly = float(hourly)
hours = float(hours)
bonus=float(bonus)
tax_rate=float(tax_rate)
salary = hourly * hours+ bonus
tax = salary * tax_rate
net = salary - tax

print("====== 11月工资条 ======")
print("姓名：" + name)
print("税前：" + str(salary) + " 元")
print("个税：" + str(tax) + " 元")
print("实发：" + str(net) + " 元")
print("制表人："+name)
