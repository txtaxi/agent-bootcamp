# Day15 代码带读

对应代码文件：`days/day15/llm_adapter.py`  
对应测试文件：`tests/test_day15_llm_adapter.py`

## 1. 今天的目标是什么

Day15 是把模型调用从业务逻辑里拆出去。

它在回答：

```python
以后换模型，为什么不应该改主流程？
```

## 2. 核心函数

1. `build_messages`
2. `parse_response`
3. `generate`

## 3. `build_messages`

它负责把业务输入整理成模型常见的 messages 结构。

## 4. `parse_response`

它负责把模型原始响应拆成业务真正关心的文本。

## 5. `generate`

它把上面两件事和模型调用串起来。

也就是说：

```python
业务层以后不要直接碰模型细节
而是走 adapter
```

## 6. 为什么重要

因为只要模型接口一变，  
你就不希望整套流程都跟着改。

## 7. 这一天真正要记什么

Day15 的一句话：

```python
把模型调用抽成可替换的一层
```
