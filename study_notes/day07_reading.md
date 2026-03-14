# Day07 代码带读

对应代码文件：`days/day07/main.py`  
对应测试文件：`tests/test_day07_main.py`

## 1. 今天的目标是什么

Day07 是第一周收口。

它不加新功能，而是在回答：

```python
这个小项目从哪里启动？
```

## 2. 核心函数

1. `parse_args`
2. `main`

## 3. `parse_args`

它负责解析最小命令行输入：

- 第一个参数当作 `user_input`
- 第二个参数当作 `thread_id`

## 4. `main`

它负责调用 `run_turn()`，  
再把内部 state 压缩成更适合外部看的结果。

所以：

```python
main = 项目统一入口
```

## 5. 为什么重要

因为到这一天为止，你的第一周代码已经不是练习碎片，  
而是一个有入口的小项目。

## 6. 这一天真正要记什么

Day07 的一句话：

```python
main 是项目入口，run_turn 是内部流程
```
