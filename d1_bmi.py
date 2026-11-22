# d1_bmi.py
# BMI 计算器 · 2026-11-16
tall=float(input("请输入身高（米）："))
weight=float(input("请输入体重（公斤）："))
BMI=round(weight/tall/tall,2)
print(BMI)
