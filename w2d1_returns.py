# W2D1 · 多返回值  w2d1_returns.py
# 目标：一个函数交回两个、三个结果，外面一次接住。
# 规则：看一段中文，写一段 Python。每写完 3-4 行按一次 F5。


# ══════════ 第一段：交回两个值 ══════════
# 步骤 1
# 定义函数 divmod_custom，接收 a 和 b 两个参数
def divmod_custom(a,b):

# 步骤 2
# 算出 a 除以 b 的商，用 // 而不是 /
# ★ // 给你整数部分，/ 给你小数
    c=a//b


# 步骤 3
# 算出余数，用 %
    d=a-b*c

# 步骤 4
# 用 return 一次交回两个值：商和余数，中间逗号隔开
# ★ 外面收到的是一个元组，不是一个数字
    return c,d

# 步骤 5
# 测试已经写好，不要改。做完上面四步按 F5。
q, r = divmod_custom(17, 5)
print(q, r)
both = divmod_custom(17, 5)
print(both)
# 想一想：q, r 这种「两个变量一起接」叫什么？both 又是什么类型？


# ══════════ 第二段：交回三个值 ══════════
# 步骤 6
# 定义函数 stats，接收一个列表 numbers
def stats(numbers):

# 步骤 7
# 先处理空列表：如果 numbers 里什么都没有，直接 return None
# ★ 为什么不是 (0, 0, 0)？因为 0 是个合法答案，None 才表示「没有答案」
# 提示：if len(numbers) == 0:
    if len(numbers) == 0:
        return None
    numbers_min=min(numbers)
    numbers_max=max(numbers)
    numbers_average=sum(numbers) / len(numbers)
    return numbers_min,numbers_max,numbers_average


# 步骤 8
# 最小值：min(numbers)


# 步骤 9
# 最大值：max(numbers)


# 步骤 10
# 平均值：先求和再除以个数
# 提示：sum(numbers) / len(numbers)


# 步骤 11
# 一次交回三个值：最小、最大、平均


# 步骤 12
# 三行测试已经写好，不要改。
print(stats([3, 1, 4, 1, 5]))
print(stats([7]))
print(stats([]))


