# Day08 代码带读

对应代码文件：`days/day08/graph_minimal.py`  
对应测试文件：`tests/test_day08_graph_minimal.py`

## 1. 今天的目标是什么

Day08 开始真正切到 LangGraph。

这一天最重要的是理解：

```python
以前是手写顺序流程
现在开始定义图，再让图执行
```

## 2. 核心内容

1. `MinimalState`
2. `echo_node`
3. `build_graph`

## 3. `echo_node`

它只是一个最小节点：

```python
输入 user_input -> 输出 reply
```

虽然简单，但它让你看清楚：

```python
节点负责更新 state 的一部分
```

## 4. `build_graph`

它负责把图搭起来：

```python
START -> echo -> END
```

然后再：

```python
compile()
```

## 5. `compile` 和 `invoke`

这是 Day08 必须弄懂的两个词。

`compile()`：

```python
把图定义变成可执行对象
```

`invoke()`：

```python
真正送入 state，执行一次图
```

## 6. 为什么重要

因为从这一天开始，你正式进入：

```python
状态图 + 节点 + 边
```

## 7. 这一天真正要记什么

Day08 的一句话：

```python
手写流程开始升级成图执行流程
```
