# Day02 代码带读

对应代码文件：`days/day02/state.py`  
对应测试文件：`tests/test_day02_state.py`

## 1. 今天的目标是什么

Day02 的目标不是继续猜用户想干嘛，  
而是开始解决一个更重要的问题：

```python
这些信息以后存到哪里？
```

所以这一天的核心是：

```python
把零散变量收成一个统一 state
```

## 2. 整体架构

文件里有 5 个对外函数：

1. `create_state`
2. `append_message`
3. `set_intent`
4. `set_result`
5. `set_error`

还有两个内部辅助函数：

- `_validate_state`
- `_validate_non_empty_string`

Day02 真正的主题不是算法，  
而是“结构”。

## 3. `create_state` 在做什么

函数签名：

```python
def create_state(user_input: str, thread_id: str = "default-thread") -> dict:
```

它会创建一个统一结构：

```python
{
    "thread_id": "...",
    "user_input": "...",
    "messages": [],
    "intent": None,
    "result": None,
    "error": None,
}
```

你可以把它理解成一张记录表：

- `thread_id`：这次会话或任务编号
- `user_input`：用户这次原始输入
- `messages`：消息历史
- `intent`：识别出来的意图
- `result`：处理结果
- `error`：错误信息

这就是 Day02 最关键的地方。

## 4. `append_message` 在做什么

它负责往 `messages` 里追加一条记录。

比如：

```python
append_message(state, "user", "weather in beijing")
```

最后 `messages` 里就会多出：

```python
{"role": "user", "content": "weather in beijing"}
```

这说明 Day02 已经开始有“对话上下文”的味道了。

## 5. `set_intent / set_result / set_error`

这三个函数可以放在一起理解。

它们的作用分别是：

- `set_intent`：写入意图
- `set_result`：写入处理结果
- `set_error`：写入错误信息

也就是说，Day02 的思想是：

```python
不要让每一步自己随便存东西
统一往 state 里写
```

## 6. 为什么 Day02 很重要

因为如果没有 state，后面流程稍微一复杂，  
你就会到处传：

```python
intent, result, error, thread_id, messages, user_input
```

很快就乱。

有了 state 之后，就统一变成：

```python
只传一个 state
```

这就是后面 LangGraph 会特别看重 state 的原因。

## 7. 测试怎么读

测试主要在看：

1. `create_state` 初始化是不是完整
2. 几个更新函数是不是都围绕同一个 state 工作
3. 坏输入会不会被挡住

## 8. 这一天真正要记什么

Day02 的一句话：

```python
把输入、过程、结果收进统一 state
```

这句话你后面会一直用到。
