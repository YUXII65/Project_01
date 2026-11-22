# W1D5 · ④ analyze.py —— 本周第二个硬门槛
# 数据：data/titanic.csv（891 行真实乘客数据，泰坦尼克号）
# 规则：看一行中文，写一行 Python。每 3-4 行按一次 F5。
# 禁止：f-string、列表推导式、lambda、pandas、sorted(key=)。用 + 和 str() 拼字符串。


# ── 步骤 1 ★ ─────────────────────────────
# 导入 csv 模块。一行。


# ── 步骤 2 ★ ─────────────────────────────
# 用 with open 打开 "data/titanic.csv"，encoding="utf-8"，newline=""。
# 里面：reader = csv.DictReader(f)
# 再一行：rows = list(reader)
# ★ 为什么套 list()：reader 是个"只能走一遍"的东西，不套 list 后面就不能重复用。
# ★ 注意缩进：reader 和 rows 这两行都在 with 里面，缩进 4 个空格。


# ── 步骤 3 ★ ─────────────────────────────
# 打印总行数。期望 891。


# ── 步骤 4 ───────────────────────────────
# 打印所有列名：遍历 rows[0].keys()，一行一个打印出来。
# 期望 15 个名字，survived 开头，alone 结尾。


# ── 步骤 5 ───────────────────────────────
# 打印前 5 行，每行只挑 3 个字段看：survived / sex / fare
# ★ 用 range(5) 取前 5 个。不要写 rows[0] 到 rows[4] 五遍。
# ★ for i in range(5) 里的 i 是数字；要拿那一行，是 rows[i]。


# ── 步骤 6 ★ ─────────────────────────────
# 统计 age 列的空值数量。期望 177。
# 做法：count = 0，然后遍历 rows，如果 row["age"] 是空字符串就 +1，最后打印。
# ★ 空值在 DictReader 里不是 None，是空字符串 ""。先打印一个空 age 的行看看长什么样。


# ── 步骤 7 ───────────────────────────────
# 按 pclass 分组，统计每组的「人数 / 票价合计 / 平均票价」。
# 准备两个字典：counts（人数）、sums（票价合计）。
# 遍历 rows，k = row["pclass"]，然后分别往两个字典里累加。
# ★ 票价累加前必须 float(row["fare"]) —— CSV 读出来一切都是字符串。
# ★ 累加写法：if k in counts: ... else: ...（D3 学过 d[k] 和 d.get(k)）
# 最后遍历 counts，打印 "1 216 18177.41 84.15" 这种三列。


# ── 步骤 8 ───────────────────────────────
# 把步骤 3 / 6 / 7 的结果同时写进 result.txt。
# 用 open("result.txt", "w", encoding="utf-8") 再套一次 with。
# ★ "w" 是覆盖写。每写一行要自己加 "\n"，不然全挤成一行。


# ── 跑不起来时看这里 ─────────────────────
# FileNotFoundError        → 当前工作目录不是 E:\Code\Project_01，找不到 data/titanic.csv
# UnicodeDecodeError       → encoding 写错了或没写
# KeyError: 'age'          → 列名拼错，或者你用了 rows["age"] 而不是 row["age"]
# TypeError: can only concatenate str → 忘了 float()
# 打印出 891 个字符             → 忘了套 list()，打印的是 reader 不是 rows
