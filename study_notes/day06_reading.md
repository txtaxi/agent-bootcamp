# Day06 代码带读

对应代码文件：`days/day06/agent_loop.py`  
对应测试文件：`tests/test_day06_agent_loop.py`

## 1. 今天的目标是什么

Day06 的重点不是新概念，  
而是终于把前 5 天串起来：

```python
输入 -> 路由 -> 工具 -> 结果 -> 回复
```

## 2. 核心函数

1. `run_turn`
2. `build_reply`
3. `run_cli`

## 3. `run_turn`

`run_turn()` 是这一天最关键的函数。

它做的事情基本就是：

1. `create_state()`
2. 记录用户消息
3. `detect_intent()`
4. 如果需要，调工具
5. 把结果写回 state
6. 用 `build_reply()` 生成最终回复
7. 再把 state 存下来

它就是一轮最小 Agent 执行。

## 4. `build_reply`

它的职责是：

```python
把结构化结果翻译成用户能读的文本
```

比如：

- `Weather reply: ...`
- `Math reply: ...`
- `Error: ...`

## 5. `run_cli`

这是最小命令行循环。  
作用是让系统可以连续处理多轮输入。

## 6. 为什么重要

因为从这一天开始，你看到的不再是散函数，  
而是一个完整处理链。

## 7. 这一天真正要记什么

Day06 的一句话：

```python
run_turn 就是一轮最小 Agent 主循环
```
