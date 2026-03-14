# Day13 代码带读

对应代码文件：`days/day13/retry_fallback.py`  
对应测试文件：`tests/test_day13_retry_fallback.py`

## 1. 今天的目标是什么

Day13 的目标是：

```python
工具失败时，不要直接把异常炸给用户
```

## 2. 核心函数

1. `safe_call_tool`
2. `fallback_reply`
3. `with_retry`

## 3. `safe_call_tool`

它负责：

```python
先把工具调用包起来
成功就返回统一成功结构
失败就返回统一错误结构
```

也就是说，异常先被“接住”。

## 4. `with_retry`

它负责：

```python
如果失败了，再试几次
```

这一步体现的是“失败不一定立刻结束”。

## 5. `fallback_reply`

如果重试之后还是失败，  
就用它把错误变成用户可读文本。

## 6. 为什么重要

因为真正稳定的系统不能只设计成功路径。

## 7. 这一天真正要记什么

Day13 的一句话：

```python
异常 -> 重试 -> 兜底
```
