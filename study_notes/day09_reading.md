# Day09 代码带读

对应代码文件：`days/day09/graph_router.py`  
对应测试文件：`tests/test_day09_graph_router.py`

## 1. 今天的目标是什么

Day09 学的是条件边。

也就是：

```python
图不再只有一条直线，而是会根据 state 走不同分支
```

## 2. 核心函数

1. `router_node`
2. `weather_node`
3. `math_node`
4. `unknown_node`
5. `route_key`

## 3. `router_node`

它做的事情其实就是把 Day01 的路由逻辑搬进图里：

```python
用户输入 -> intent
```

## 4. `route_key`

它特别重要，因为它不是业务节点，  
它是“决定下一条边去哪”的条件函数。

例如：

- `intent == weather` -> 去 `weather`
- `intent == math` -> 去 `math`
- 其他 -> 去 `unknown`

## 5. 图结构

```python
START -> router -> weather / math / unknown -> END
```

## 6. 为什么重要

因为这一天开始，你会真正看到：

```python
state 不只是存数据，还会控制流程
```

这就是你之前问的“状态机和流程设计”开始落地的地方。

## 7. 这一天真正要记什么

Day09 的一句话：

```python
图开始根据状态做分支决策
```
