# Day17 代码带读

对应代码文件：`days/day17/hitl_flow.py`  
对应测试文件：`tests/test_day17_hitl.py`

## 1. 今天的目标是什么

Day17 的主题是 HITL：人在回路。

它在回答：

```python
哪些动作不应该自动直接执行？
```

## 2. 核心函数

1. `needs_approval`
2. `wait_for_approval`
3. `resume_after_approval`

## 3. `needs_approval`

它负责判断：

```python
这是不是高风险动作
```

如果是高风险动作，就进入“等待批准”状态。

## 4. `wait_for_approval`

它负责模拟已经等到了人工审批结果。

## 5. `resume_after_approval`

它负责根据审批结果决定：

- 继续执行
- 或者拒绝终止

## 6. 为什么重要

因为真实 Agent 不是越自动越好。

像：

- 删除
- 转账
- 付款
- 停服务

这种动作，通常要有人点头。

## 7. 这一天真正要记什么

Day17 的一句话：

```python
高风险动作需要暂停，等人批准后再恢复流程
```
