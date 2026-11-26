# W2D4 · 2026-11-26  脚本到底由谁运行？
# 规格：AI-Career-Training/03_Exercises/W2D4_任务卡.md §3。这里不给步骤。
#
# 输出必须恰好 5 行，前缀固定：
#   解释器: <sys.executable>
#   工作目录: <os.getcwd()>
#   脚本路径: <os.path.abspath(__file__)>
#   数据文件存在: True / False
#   第 5 行 —— 存在：打印 data/titanic.csv 的前 2 行
#              不存在：打印「找不到 data/titanic.csv，当前目录: <cwd>」，不许崩
#
# 硬约束：只用标准库；读 CSV 必须用相对路径；不许 os.chdir；退出码 0。
#
# 动笔前先回答自己一个问题：哪一行代码能证明「我现在站在哪个目录」？
import os
import sys

a=os.path.exists("data/titanic.csv")
print("解释器: "+sys.executable)
print("工作目录: "+os.getcwd())
print("脚本路径: "+os.path.abspath(__file__))
print("数据文件存在: "+str(a))
if a==True:
    lines=open("data/titanic.csv", encoding="utf-8").readlines() 

    print(lines[:2])
else:
    print("找不到 data/titanic.csv,当前目录："+os.getcwd())
