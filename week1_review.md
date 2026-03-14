# 第1周复盘

## 这一周做了什么

第一周从零开始，手写了一个最小 Agent 骨架。

主线是：

```python
Day01: 路由
Day02: state
Day03: memory
Day04: http retry
Day05: tools
Day06: agent loop
Day07: main entry
```

---

## 这一周真正搭出来了什么

到 Day07 为止，这个项目已经具备：

1. 能识别最小意图
2. 能把数据收进统一 state
3. 能按 thread_id 保存和恢复
4. 能做最小 HTTP 失败处理
5. 能做工具分发
6. 能完成一轮输入到回复
7. 能通过统一入口启动

---

## 这一周最该记住的主线

不要分别去背每一天的细节，  
只记这条主线：

```python
用户输入
-> detect_intent
-> dispatch_tool
-> 写入 state
-> build_reply
-> save_state
-> main 统一输出
```

---

## 这一周最容易混淆的点

### `route` 和 `run_turn`

- `route` 更小，只负责路由
- `run_turn` 更完整，负责一轮处理

### `run_turn` 和 `main`

- `run_turn` 是内部执行流程
- `main` 是外部统一入口

### `state` 和 `reply`

- `state` 是内部结构化上下文
- `reply` 是给用户看的最终文本

---

## 这一周学到的最关键习惯

1. 统一返回结构
2. 外部输入先校验
3. 用 state 管理上下文
4. 用单入口串起流程

---

## 下一周要开始关注什么

下一周如果继续往下做，重点一般会从“手写小骨架”转向：

1. 节点拆分
2. 图结构组织
3. 条件分支
4. 多步状态流转

也就是说，第一周是打底，  
第二周会更接近真正的 LangGraph 思路。
