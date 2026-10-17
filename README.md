# Python 训练

这是我的个人 Python 编程训练记录，从基础语法练习到完整的异常片段提取与数据持久化。

## 目录结构

```
.
├── README.md            # 本说明文件
├── time_segments.json   # 异常时间片段数据示例
└── python训练/           # 按天划分的训练代码
    ├── day1_1_jointchecking.py
    ├── day1_making.py
    ├── day2_1.py
    ├── day3_1.py
    ├── day3_2.py
    ├── day3_3.py
    ├── day4_1.py
    ├── day4_2.py
    ├── day4_3.py
    ├── day4_4.py
    ├── day5_1.py
    ├── day5_2.py
    ├── day5_3.py
    ├── day6_1.py
    └── day6_2.py
```

## 训练内容

### Day 1 — 基础：关节角度检查
- `day1_1_jointchecking.py`：遍历关节角度列表，统计超过阈值的"极端关节"数量。
- `day1_making.py`：将检查逻辑封装为函数 `check_joints()`，练习函数定义与返回值处理。

### Day 2 — 状态与速度双重检查
- `day2_1.py`：在角度阈值基础上增加速度阈值，练习字典遍历与条件判断。

### Day 3 — 状态字典与帧序列
- `day3_1.py`：使用字典表示多个关节的状态。
- `day3_2.py` / `day3_3.py`：用元组序列表示多帧状态，练习对帧序列的处理。

### Day 4 — 帧序列与异常状态统计
- `day4_1.py`：对肩/肘/腕多关节帧序列进行处理。
- `day4_2.py`：统计连续异常状态的计数。
- `day4_3.py` / `day4_4.py`：扩展到手指（拇指/食指/中指）的多帧状态分析。

### Day 5 — 异常片段检测
- `day5_1.py`：从状态序列中提取异常片段。
- `day5_2.py`：多手指帧序列的异常片段处理。
- `day5_3.py`：封装为函数 `find_abnormal_segments()`，返回异常片段。

### Day 6 — JSON 读写与时间转换
- `day6_1.py`：使用 `json` 模块读写数据文件。
- `day6_2.py`：帧索引与时间戳的换算（`frame_to_time()`），输出时间片段（对应根目录的 `time_segments.json`）。

## 运行方式

所有文件均为纯 Python 脚本，直接运行即可：

```bash
cd python训练
python day1_1_jointchecking.py
```

## 说明

- 状态 `A` / `B` / `D` 等字母代表关节的不同状态等级，具体含义以各文件内注释为准。
- 本仓库为个人学习用途，随学习进度持续更新。
