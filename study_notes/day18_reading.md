# Day18 代码带读

对应代码文件：`days/day18/multi_tool_pipeline.py`  
对应测试文件：`tests/test_day18_pipeline.py`

## 1. 今天的目标是什么

Day18 的主题是多工具流水线。

主线是：

```python
检索 -> 计算 -> 总结
```

## 2. 核心步骤

1. `retrieve_step`
2. `calculate_step`
3. `summarize_step`

## 3. `retrieve_step`

先产出一个结构化中间结果。

## 4. `calculate_step`

消费上一步的结果，再产出新的中间结果。

## 5. `summarize_step`

最后把中间结果整理成最终可读文本。

## 6. 为什么重要

因为真实 Agent 很多都不是一步完成任务，  
而是：

```python
前一步的结果变成后一步的输入
```

这一天练的就是这个能力。

## 7. 这一天真正要记什么

Day18 的一句话：

```python
多步任务最重要的是中间状态的稳定传递
```
