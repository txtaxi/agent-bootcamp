# Day03 代码带读

对应代码文件：`days/day03/memory.py`  
对应测试文件：`tests/test_day03_memory.py`

## 1. 今天的目标是什么

Day03 在做的事情不是新业务逻辑，  
而是：

```python
让 Day02 的 state 能记住
```

也就是：

```python
state 可以保存到文件
state 也可以再从文件读回来
```

## 2. 核心函数

1. `get_state_path`
2. `save_state`
3. `load_state`
4. `list_threads`

## 3. `get_state_path`

它的作用很简单：

```python
根据 thread_id 生成对应文件路径
```

也就是说：

```python
每个 thread_id 对应一个 JSON 文件
```

## 4. `save_state`

这个函数会把当前的 state 存成 JSON。

它做的事情是：

1. 校验 state 是否完整
2. 算出文件路径
3. 确保目录存在
4. 把 state 写入 JSON

这意味着 Day03 开始，state 不再只是临时变量。

## 5. `load_state`

它的作用刚好相反：

```python
给我 thread_id，我把之前保存的 state 读回来
```

如果文件不存在，就报错。

## 6. `list_threads`

它负责列出已经保存过哪些 thread。

这一步让你看到：

```python
系统开始具备最小的“会话索引能力”
```

## 7. 为什么 Day03 很重要

因为如果系统每次重启都忘光之前状态，  
那很多多轮任务就做不下去。

所以 Day03 真正做的是：

```python
给系统加最小记忆
```

## 8. 测试怎么读

测试主要覆盖：

1. 保存后再读，内容是否一致
2. 路径生成是否正常
3. 文件不存在时是否报错
4. 已保存线程是否能列出来

## 9. 这一天真正要记什么

Day03 的一句话：

```python
用 thread_id 把 state 记住
```
