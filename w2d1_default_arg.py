# W2D1 · 默认参数陷阱  w2d1_default_arg.py
# 目标：亲手撞一次「函数记住了上一次的结果」，再用 None 修好。
# 规则：看一段中文，写一段 Python。每写完 3-4 行按一次 F5。


# ══════════ 第一段：先撞坑 ══════════
# 步骤 1
# 定义函数 add，接收两个参数 item 和 bucket
# bucket 的默认值写成空列表 []
# 形状：def add(item, bucket=[]):
# 注意这一行末尾是冒号。
###def add(item, bucket=[]):
    

# 步骤 2
# 函数体缩进 4 空格：把 item 塞进 bucket 末尾
# 用 bucket.append(item)
   # bucket.append(item)

# 步骤 3
# 交回 bucket。用 return，不要 print。

   # return bucket
# 步骤 4
# 下面两行测试已经写好，不要改。上面三步写完就按 F5。
# 先在心里猜：两次分别打印什么？把猜测写在这行注释里，再看实际输出。
#   我的猜测：第一次 ____  第二次 ____
#print(add("苹果"))
#print(add("香蕉"))


# ══════════ 第二段：修好它 ══════════
# 步骤 5
# 把 bucket 的默认值从 [] 改成 None
def add(item, bucket=None):

# 步骤 6
# 函数体第一行加一个判断：如果 bucket 是 None，就给它一个新建的空列表
# 提示：if bucket is None:
# 判断用 is，不是 ==
    if bucket is None:
        bucket=[]
    bucket.append(item)
    return bucket
print(add("苹果"))
print(add("香蕉"))
# 步骤 7
# 再按一次 F5。输出变了吗？变成什么？


# ══════════ 第三段：说清为什么 ══════════
# 步骤 8
# 在文件最下面用一行中文注释回答：
# 为什么 [] 会「记住」上一次，而 None 不会？
#
# 我的答案：列表在函数创建时就有，一直就是bucket，同一个，写none了，他在创建时就是none，本次调用在创建一个[]，懂了
def add_bug(item, bucket=[]):
    bucket.append(item)
    return bucket
print(add_bug("苹果"))
print(add_bug("香蕉"))

def add_proof(item, bucket=[]):
    print(id(bucket))
    bucket.append(item)
    return bucket
print(add_proof("苹果"))
print(add_proof("香蕉"))
print(add_proof.__defaults__)

print(add("橘子", ["已有的"]))
