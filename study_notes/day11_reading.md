# Day11 代码带读

对应代码文件：`days/day11/graph_memory_inmem.py`  
对应测试文件：`tests/test_day11_inmem.py`

## 1. 今天的目标是什么

Day11 学的是 InMemory Checkpointer。

也就是：

```python
图状态如何按 thread_id 在内存里保存和恢复
```

## 2. 核心函数

1. `build_graph_with_inmem`
2. `invoke_with_thread`

## 3. `build_graph_with_inmem`

它的关键点不在节点，而在：

```python
compile(checkpointer=InMemorySaver())
```

这说明图执行状态会被保存到内存 checkpointer 里。

## 4. `invoke_with_thread`

它最关键的一句是：

```python
config={"configurable": {"thread_id": ...}}
```

这里的 `thread_id` 就是会话隔离键。

## 5. 为什么同 thread 能延续

因为同一个 `thread_id` 再次调用时，  
checkpointer 会把之前那条状态取回来继续跑。

## 6. 为什么不同 thread 会隔离

因为换了 `thread_id`，  
系统就会当成一条新会话。

## 7. 这一天真正要记什么

Day11 的一句话：

```python
同一个图能像“记住上下文”，靠的是 checkpointer + thread_id
```
