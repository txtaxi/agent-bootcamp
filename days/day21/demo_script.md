# Demo Script

## 目标

演示这个最小毕业项目已经具备：

1. 输入到回复闭环
2. 路由与工具调用
3. 图执行
4. 批量评测

## 手动演示建议

### 1. 天气输入

输入：

```text
weather in beijing
```

预期：

```text
Weather reply: beijing is sunny
```

### 2. 数学输入

输入：

```text
1 + 2 * 3
```

预期：

```text
Math reply: 7
```

### 3. 未知输入

输入：

```text
hello
```

预期：

```text
Error: unknown intent
```

## 结论

这套最小毕业项目已经能够展示：

```python
输入 -> 图 -> 工具 -> 回复 -> 评测
```
