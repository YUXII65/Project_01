# Project_01

读一份 891 行的泰坦尼克号乘客名单，按舱位算出人数、票价合计和平均票价。

> 2026 年 11 月第 1 周的 Python 学习记录。代码是手打的，不是复制粘贴的。

## 怎么运行

只用 Python 标准库，不需要 `pip install`。需要 Python 3.8 以上。

```bash
cd E:\Code\Project_01
python d5_read_demo.py
```

其他脚本同理，换文件名即可：

```bash
python d1_salary.py
python d2_prime.py
python d3_15_topwords.py
```

## 依赖

- Python 3.8+
- 只用标准库（`csv`），无第三方包
- 数据集 `data/titanic.csv` 已随仓库提供，无需另外下载

## 文件清单

| 文件 | 干什么 | 哪天写的 |
|---|---|---|
| `d1_salary.py` | 输入时薪/工时/奖金/税率，输出一张工资条（税前、个税、实发） | D1 |
| `d1_intro.py` | 输入姓名/专业/目标，拼成三句英文自我介绍 | D1 |
| `d1_bmi.py` | 输入身高体重，算 BMI（保留 2 位小数） | D1 |
| `d1_temp.py` | 摄氏度转华氏度 | D1 |
| `d2_grade.py` | 循环 5 次输入成绩，按 90/80/60 分档输出 A/B/C/D，处理缺考与非法输入 | D2 |
| `d2_prime.py` | 判断一个数是不是质数（`for` + `break`） | D2 |
| `d2_prime_retest.py` | 质数判断的重测版，关掉 AI 重写一遍 | D2 |
| `d2_countdown.py` | 用 `while` 从 10 倒数，到 0 打印「发射」 | D2 |
| `d3_wordcount.py` | 统计一段英文里每个词出现几次，只打印出现超过 1 次的 | D3 |
| `d3_15_topwords.py` | 把多句话拼起来，输出出现次数最多的前 3 个词 | D3 |
| `d3_01_dedupe.py` | 列表去重，两种写法：不用 `set` / 用 `set` | D3 |
| `d3_02_stats.py` | 求一组数的最大值、最小值、平均值 | D3 |
| `d3_04_charcount.py` | 统计字符串里每个字符出现几次 | D3 |
| `d3_08_mostcommon.py` | 找出一组数里出现次数最多的那个 | D3 |
| `d5_read_demo.py` | 读 CSV：打印行数与列名、统计空值、按舱位分组算人数/票价合计/平均票价 | D5 |
| `analyze.py` | D5 的练习骨架，只有中文步骤注释，代码未填 | D5 |
| `utils.py` | 跨文件练习：函数定义（骨架，未填） | D4 |
| `main.py` | 跨文件练习：调用 `utils.py`（骨架，未填） | D4 |
| `data/titanic.csv` | 891 行泰坦尼克号乘客数据，15 列（seaborn 公开数据集） | D5 |
| `data/edge.csv` | 教学用：引号内含逗号，用来证明 `split(",")` 会切错 | D5 |
| `data/utf8_test.csv` | 教学用：中文内容，用来制造 `UnicodeDecodeError` | D5 |

## 已知限制

1. **三个 D3 脚本输出是错的，还没修。** `d3_01_dedupe.py`、`d3_02_stats.py` 把列表元素当索引用（`text[i]`），`d3_08_mostcommon.py` 打印的是出现次数而不是那个元素本身。根因是同一个：`for i in 列表` 里的 `i` 是元素本身，不是下标。
2. **必须在 `E:\Code\Project_01` 目录下运行。** 代码用相对路径 `data/titanic.csv` 读数据，换个目录就 `FileNotFoundError`。
3. **没有异常处理。** 输入非数字（比如在 `d1_salary.py` 里输 `abc`）会直接抛 `ValueError` 崩溃，不会提示重输。
4. **`utils.py` / `main.py` / `analyze.py` 是空骨架。** 只有中文注释，没有可执行代码，跑起来没有任何输出。

## 我学到了什么

<!-- 明早用 3 分钟改成你自己的说法 -->

CSV 是逗号分隔的纯文本，代码可以直接读它。
处理一份 891 行的真实数据，不需要任何第三方库。
真正卡住我的不是逻辑，是语法：缩进、引号、`return` 该放在哪一行。
