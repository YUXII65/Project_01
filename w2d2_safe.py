# W2D2 · 从零写三个安全函数  w2d2_safe.py
# 目标：把今天学的 try 用进真代码。三个函数，按顺序做，每做完一个按 F5。
# 规则：中文是骨架，你只翻译成 Python。每 3–4 行按一次 F5。


# ══════════════════════════════════════════════════════════
# 第一个 · safe_int（5 分钟，热身）
# ══════════════════════════════════════════════════════════
# 步骤 1
# 定义函数 safe_int，接收两个参数：s 和 default
# default 的默认值写 0
def safe_int(s,default=0):
    try:
        s=int(s)
        return s
    except ValueError:
        return default
    
# 步骤 2
# 用 try 试着把 s 转成整数，成功就 return 出来


# 步骤 3
# 用 except ValueError 接住失败，return default
# ★ 只接 ValueError，不要写 except Exception，也不要用 pass


# 步骤 4
# 下面四行测试已经写好，不要改。做完上面三步按 F5。
# 先预测四个输出，写在注释里。
#   我的预测：__42__  __0__  __-1__  __-5__
print(safe_int("42"))
print(safe_int("abc"))
print(safe_int("abc", -1))
print(safe_int("-5"))


# ══════════════════════════════════════════════════════════
# 第二个 · read_number（15 分钟，今天最硬的一题）
# ══════════════════════════════════════════════════════════
# 目标：一直问用户要数字，直到他真的给出一个数字为止。给错不能崩，要重问。
#
# 步骤 5
# 定义函数 read_number，接收一个参数 prompt（要显示给用户的话）
def read_number(prompt="给出数字"):

# 步骤 6
# 写一个循环，让它可以一直问下去
# ★ 循环的退出条件是「拿到数字」，不是「问够几次」
    while True:
        n=input(prompt)
        try:
            n=int(n)
            return n
        except ValueError:
            print("那不是一个整数，再试一次")

# 步骤 7
# 循环体里：用 input(prompt) 收一行输入，试着转成整数
# 成功 → return 这个整数（直接 return 就跳出循环了，不需要 break）


# 步骤 8
# 失败 → 打印一句提示，比如「那不是一个整数，再试一次」，然后让循环继续


# 步骤 9
# 下面这行测试已经写好，不要改。
# 跑起来以后在 IDLE 的 Shell 窗口里手动输入：先输 abc，再输 3.5，最后输 42
n = read_number("请输入一个整数：")
print("收到:", n, "它的两倍是", n * 2)


# ══════════════════════════════════════════════════════════
# 第三个 · safe_divide（5 分钟）
# ══════════════════════════════════════════════════════════
# 目标：除零不崩，返回 None 并说清原因。
#
# 步骤 10
# 定义函数 safe_divide，接收 a 和 b

def safe_divide(a,b):
# 步骤 11
# 用 try 算 a / b，成功就 return 结果
    try:
        c=a/b
        return c
    except ZeroDivisionError:
        print("不能用0做除数")
        return None


# 步骤 12
# 用 except ZeroDivisionError 接住，先打印一句原因，再 return None
# ★ 注意顺序：print 要在 return 之前，否则 return 走了 print 就没机会执行


# 步骤 13
# 三行测试已经写好，不要改。先预测输出。
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(0, 5))


# ══════════════════════════════════════════════════════════
# 收尾 · 用一行中文注释回答（这题明天三问会考）
# ══════════════════════════════════════════════════════════
# 什么情况下该用 if 判断，什么情况下该用 try？
#
# 我的答案：需要默认数据确认，先用try。如果要排除错误数据，用if排除
