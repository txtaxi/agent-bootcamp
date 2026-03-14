# Day19 代码带读

对应代码文件：`days/day19/eval_runner.py`  
对应数据文件：`days/day19/eval_cases.json`  
对应测试文件：`tests/test_day19_eval.py`

## 1. 今天的目标是什么

Day19 的重点不再是新工具或新图，  
而是开始做评测。

它在回答：

```python
你怎么量化自己的 Agent 现在到底行不行？
```

## 2. 核心函数

1. `run_case`
2. `score_case`
3. `summarize_report`

## 3. `run_case`

它负责真正跑一条评测样例，
并记录实际输出和延迟。

## 4. `score_case`

它负责给单条结果打分：

```python
expected == actual ? 成功 : 失败
```

## 5. `summarize_report`

它负责汇总多条结果，得出：

- 总数
- 成功数
- 成功率
- 平均延迟

## 6. 为什么重要

因为从这一天开始，你不再只靠“感觉好像能跑”，  
而是开始有 baseline 报告。

## 7. 这一天真正要记什么

Day19 的一句话：

```python
把主观感觉变成可量化指标
```
