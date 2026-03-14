# 21 天项目总复盘

## 1. 这 21 天你到底做了什么

这 21 天不是在零散学很多小知识点，  
而是在一点点搭一个最小 Agent 系统。

如果压缩成一条主线，就是：

```python
用户输入
-> 清洗 / 路由
-> 统一 state
-> 工具 / 节点 / 图执行
-> 中间结果更新
-> 回复
-> 会话记忆 / 恢复
-> 错误处理
-> 评测
-> 工程化收口
```

也就是说，你不是在单独学 Python 小题，  
而是在一步步拆开 Agent 背后的基本部件。

---

## 2. 三周分别在学什么

### 第一周：手写版 Agent 骨架

- Day01：最小路由
- Day02：统一 state
- Day03：JSON 记忆
- Day04：HTTP 失败处理
- Day05：工具系统与分发
- Day06：主循环
- Day07：统一入口

第一周的核心不是 LangGraph，  
而是先理解：

```python
如果没有框架，你自己到底要手写什么
```

### 第二周：LangGraph 与状态流转

- Day08：最小图
- Day09：条件边
- Day10：把手写 Agent 迁到图
- Day11：InMemory checkpointer
- Day12：SQLite checkpointer
- Day13：错误恢复与兜底
- Day14：第二周整合

第二周的核心是：

```python
把前面手写版思路，迁成图执行和状态流转模型
```

### 第三周：更接近真实 Agent 的工程骨架

- Day15：LLM adapter
- Day16：LLM + tool calling 闭环
- Day17：HITL 人在回路
- Day18：多工具流水线
- Day19：评测与 baseline
- Day20：配置 / 日志 / 启动
- Day21：毕业项目收口

第三周的核心是：

```python
从“会跑”走向“更像一个可展示、可维护的项目”
```

---

## 3. 你现在应该已经能理解的核心概念

### 1. `state`

`state` 不是一个花哨名词，  
本质就是：

```python
系统当前掌握的结构化信息
```

例如：

- 用户输入
- 当前意图
- 中间结果
- 错误
- 消息历史
- thread_id

### 2. 流程

流程就是：

```python
下一步该做什么
```

比如：

- 先路由
- 再调工具
- 再生成回复
- 如果失败就重试

### 3. 状态机味道

状态机不是很玄，
你可以把它理解成：

```python
不同状态下，系统走不同路径
```

例如：

- `intent=weather` 走天气分支
- `intent=math` 走数学分支
- `unknown` 走错误分支

### 4. `thread_id`

它的作用不是“随便起个名字”，  
而是：

```python
区分不同会话 / 不同状态恢复上下文
```

### 5. checkpointer

它的本质是：

```python
帮图保存和恢复状态
```

### 6. tool calling

本质不是“模型会魔法”，  
而是：

```python
模型先决定要不要调工具
系统再去执行工具
```

### 7. HITL

本质是：

```python
不是所有动作都要自动执行
关键动作可以暂停，等人批准
```

---

## 4. 手写版和 LangGraph 版到底是什么关系

你现在可以这样理解：

### Day01-Day07

是手写版 Agent 基础。

### Day08 以后

是 LangGraph 版 Agent 基础。

这两部分不是互相推翻，  
而是：

```python
前者教你原理
后者教你框架里的组织方式
```

所以前 7 天没有“没用”，  
它们真正的价值在于：

```python
让你知道 LangGraph 到底在替你接管什么问题
```

---

## 5. 这个项目现在的目录结构

现在代码已经整理过，主要结构是：

```text
agent-bootcamp/
  days/
    day01/
    day02/
    ...
    day21/
  tests/
  study_notes/
  week1_review.md
  week2_review.md
  FINAL_REVIEW_21_DAYS.md
```

你后面最重要的 3 个目录就是：

- `days/`：看代码
- `tests/`：看行为验证
- `study_notes/`：看带读说明

---

## 6. 这个项目怎么启动

当前这是一个“教学型最小 Agent 项目”，
不是完整商业产品，但已经可以运行、测试、演示。

### 1. 跑全量测试

```powershell
Set-Location D:\Study\Agent\StudyPlan\agent-bootcamp
uv run pytest tests -q
```

### 2. 跑毕业项目最小 demo

```powershell
Set-Location D:\Study\Agent\StudyPlan\agent-bootcamp
uv run python -c "from days.day21.capstone_agent import run_demo; print(run_demo('weather in beijing'))"
```

### 3. 跑批量评测

```powershell
Set-Location D:\Study\Agent\StudyPlan\agent-bootcamp
uv run python -c "from days.day21.capstone_agent import run_batch_eval; print(run_batch_eval()['report'])"
```

---

## 7. 这个项目现在怎么用

最主要的入口在：

`days/day21/capstone_agent.py`

当前最常用的两个函数：

### `run_demo(user_input)`

作用：

```python
给一句输入，返回最小演示结果
```

输出结构大概是：

```python
{
    "intent": "...",
    "reply": "...",
    "error": ...
}
```

### `run_batch_eval()`

作用：

```python
批量跑评测 case，并返回报告
```

---

## 8. 这个项目现在“能不能用”

答案是：

```python
能用，但它是教学版 / 演示版，不是生产版
```

### 现在已经能做的

1. 能跑最小路由
2. 能跑图版 Agent
3. 能演示 tool calling
4. 能演示 thread_id 和记忆
5. 能演示 InMemory / SQLite checkpointer
6. 能演示 HITL
7. 能跑最小评测
8. 能在新机器上更容易配置和启动

### 现在还不是完整产品的地方

1. 没接真实 LLM API
2. 工具大多是 mock / 教学版
3. 检索不是正式 RAG 系统
4. 评测集规模很小
5. 还没有真正的 Web 服务或 CLI 产品入口
6. 日志和配置只是最小工程化版本

所以更准确地说：

```python
它现在是“可运行、可测试、可演示、可学习”的最小 Agent 项目
```

---

## 9. 推荐阅读顺序

如果你以后回头复习，建议按这个顺序：

### 第一轮：先抓主线

1. `study_notes/day01_reading.md`
2. `study_notes/day02_reading.md`
3. `study_notes/day06_reading.md`
4. `study_notes/day08_reading.md`
5. `study_notes/day10_reading.md`
6. `study_notes/day11_reading.md`
7. `study_notes/day16_reading.md`
8. `study_notes/day21_reading.md`

这一轮只抓大框架。

### 第二轮：补关键机制

1. `study_notes/day03_reading.md`
2. `study_notes/day04_reading.md`
3. `study_notes/day05_reading.md`
4. `study_notes/day09_reading.md`
5. `study_notes/day12_reading.md`
6. `study_notes/day13_reading.md`
7. `study_notes/day17_reading.md`
8. `study_notes/day19_reading.md`

### 第三轮：按代码对照读

读法是：

```text
days/dayXX 代码
-> study_notes/dayXX_reading.md
-> tests/test_dayXX_*.py
```

---

## 10. 如果以后要把这个教学项目升级成“更真实的项目”

最合理的升级路线大概是这样：

### 第一步：接真实模型

把 Day15 的 adapter 从 fake model 换成真实模型 API。

例如：

- OpenAI
- Anthropic
- 本地模型

### 第二步：把 mock 工具替换成真实工具

现在的天气、计算、检索都很教学版。  
以后可以逐步换成：

- 真天气 API
- 真搜索 / 检索
- 真数据库 / 真业务接口

### 第三步：把 Day16 和 Day18 图化

现在有些地方还是函数串联思路，  
后面可以迁成更完整的 LangGraph 多节点图。

### 第四步：统一状态结构

现在不同天的例子里 `state` 结构是分开练习的。  
以后真实项目里最好收成一套统一 schema。

### 第五步：加真正的服务入口

例如：

- CLI
- FastAPI
- Web UI

### 第六步：补更像真实项目的评测

Day19 现在只是 baseline 骨架。  
以后可以补：

- 更多 case
- 分类报告
- 失败样例分析
- 回归对比

---

## 11. 你现在最值得记住的 10 句话

1. Agent 不神秘，本质是 `LLM + state + tools + flow`。
2. 前 7 天是在手写版里理解底层原理。
3. 第 8 天以后是在 LangGraph 里学图执行方式。
4. `state` 是整个系统的核心信息容器。
5. `thread_id` 是会话隔离和状态恢复的关键。
6. checkpointer 不是模型记忆，而是系统状态保存。
7. 工具调用的重点不是“会不会调”，而是“怎么稳定调”。
8. 失败路径和成功路径同样重要。
9. 评测不是感觉好，而是 baseline。
10. 一个能跑的 demo 不等于一个可交付项目，工程化还要补配置、日志、评测和启动。

---

## 12. 最后一句总结

如果只留一句话，你应该记这个：

```python
这 21 天不是在学一堆散碎代码，
而是在一步步理解：一个 Agent 系统到底是怎么从输入、状态、流程、工具、记忆，一直走到可演示项目的。
```
