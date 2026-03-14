# Day12 代码带读

对应代码文件：`days/day12/graph_memory_sqlite.py`  
对应测试文件：`tests/test_day12_sqlite.py`

## 1. 今天的目标是什么

Day12 是把 Day11 的内存记忆升级成 SQLite 落盘记忆。

它在回答的问题是：

```python
程序重启以后，状态还能不能接着恢复？
```

## 2. 核心函数

1. `init_sqlite_path`
2. `build_graph_with_sqlite`

## 3. `init_sqlite_path`

它负责准备 SQLite 文件路径。

也就是说，它先解决：

```python
状态落盘落到哪
```

## 4. `build_graph_with_sqlite`

它的重点在这里：

```python
sqlite3.connect(...)
SqliteSaver(conn)
compile(checkpointer=...)
```

这意味着图状态不再只是存内存，  
而是写入 SQLite 文件。

## 5. 与 Day11 的区别

Day11：

```python
只在当前进程里记住
```

Day12：

```python
重新建图后还能用同一个 sqlite 文件恢复
```

## 6. 为什么重要

因为真实系统通常不能只靠进程内内存，
而需要真正落盘。

## 7. 这一天真正要记什么

Day12 的一句话：

```python
状态从“内存记忆”升级成“可落盘恢复”
```
