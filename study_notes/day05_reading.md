# Day05 代码带读

对应代码文件：`days/day05/tools.py`  
对应测试文件：`tests/test_day05_tools.py`

## 1. 今天的目标是什么

Day05 的目标是：

```python
把多个能力收成一个统一工具系统
```

## 2. 核心函数

1. `tool_weather`
2. `tool_calc`
3. `tool_time`
4. `dispatch_tool`

## 3. 三个工具函数

`tool_weather`：模拟天气能力。  
`tool_calc`：模拟计算能力。  
`tool_time`：模拟时间能力。

每个工具本质上都是：

```python
输入 -> 返回统一结构
```

## 4. `dispatch_tool`

这一天真正最重要的是它。

它的工作是：

```python
根据工具名，决定调用哪个工具函数
```

所以从 Day05 开始，你的系统已经有“工具分发”味道了。

## 5. 为什么重要

因为 Agent 后面通常不会只用一个能力。  
有了分发器，后面很多工具都能统一挂进去。

## 6. 测试怎么读

测试主要验证：

1. 三个工具各自能不能工作
2. `dispatch_tool()` 能不能正确分发
3. 未知工具会不会报错

## 7. 这一天真正要记什么

Day05 的一句话：

```python
多个工具统一从 dispatch_tool 入口调度
```
