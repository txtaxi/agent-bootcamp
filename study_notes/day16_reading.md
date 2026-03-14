# Day16 代码带读

对应代码文件：`days/day16/llm_tool_loop.py`  
对应测试文件：`tests/test_day16_llm_tool_loop.py`

## 1. 今天的目标是什么

Day16 开始让模型真正驱动工具调用。

主线是：

```python
模型先判断 -> 系统执行工具 -> 模型再组织最终回答
```

## 2. 核心函数

1. `decide_tool_call`
2. `execute_tool_call`
3. `finalize_answer`

## 3. `decide_tool_call`

它先让模型判断：

```python
这次要不要调工具
```

如果模型输出的是约定好的 `TOOL:...` 格式，  
就说明要调用工具。

## 4. `execute_tool_call`

它负责把模型决策变成真正的工具执行。

## 5. `finalize_answer`

它负责把“用户问题 + 工具结果”再交给模型，
让模型生成最终自然语言回答。

## 6. 为什么重要

因为到这一天为止，你终于看到：

```python
LLM 不只是回答，还先决定要不要做动作
```

这就是 Agent 和普通聊天最接近本质差异的地方之一。

## 7. 这一天真正要记什么

Day16 的一句话：

```python
模型先决策，系统再执行，最后模型再收口
```
