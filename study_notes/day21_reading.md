# Day21 代码带读

对应代码文件：`days/day21/capstone_agent.py`  
对应说明文件：`days/day21/README.md`  
对应演示脚本：`days/day21/demo_script.md`  
对应测试文件：`tests/test_day21_capstone.py`

## 1. 今天的目标是什么

Day21 是最后一天。  
这一天不是再引入新概念，而是把前 20 天收成一个“可演示、可测试、可解释”的最小毕业项目。

## 2. 核心函数

1. `build_capstone_graph`
2. `run_demo`
3. `run_batch_eval`

## 3. `build_capstone_graph`

它直接复用了 Day10 的图版 Agent。

这说明毕业项目不是推倒重来，而是：

```python
把之前已经做好的骨架组合起来
```

## 4. `run_demo`

它负责做最小单次演示：

```python
输入一句话 -> 跑图 -> 返回 intent / reply / error
```

这就是最适合拿来 demo 的入口。

## 5. `run_batch_eval`

它负责复用 Day19 的评测器，批量跑 case，并输出总结报告。

所以毕业项目不只是“能演示”，还要“能量化验证”。

## 6. 为什么 Day21 是收口

因为到这里为止，你已经把前面的这些能力都串过了：

- 路由
- state
- memory
- tools
- graph
- checkpointer
- retry
- LLM adapter
- tool loop
- HITL
- pipeline
- eval
- config/logging

Day21 做的不是新发明，而是：

```python
把这些东西收成一个最小项目壳
```

## 7. 这一天真正要记什么

Day21 的一句话：

```python
毕业项目不是新系统，而是把前 20 天的骨架收成可展示成果
```
