# Day10 代码带读

对应代码文件：`days/day10/graph_agent.py`  
对应测试文件：`tests/test_day10_graph_agent.py`

## 1. 今天的目标是什么

Day10 是把 Day06 的手写 Agent 迁到 LangGraph。

换句话说：

```python
不再手写主循环，而是用图复刻同样的核心行为
```

## 2. 核心节点

1. `router_node`
2. `tool_node`
3. `final_node`

## 3. `router_node`

它负责先识别当前输入的意图。

## 4. `tool_node`

它负责按意图调用工具：

- 天气走天气工具
- 数学走计算工具

## 5. `final_node`

它负责把当前 state 里的结构化结果变成最终回复。

也就是说，它承担的是 Day06 里 `build_reply()` 的角色。

## 6. 图结构

```python
START -> router -> tool 或 final -> final -> END
```

这已经很像一个最小 Agent 图了。

## 7. 为什么重要

因为 Day10 真正让你看到：

- 手写版流程长什么样
- 图版流程长什么样
- 两者可以怎么一一对应

## 8. 这一天真正要记什么

Day10 的一句话：

```python
把手写版 Agent 迁到图执行模型里
```
