# Agent Bootcamp（Agent 训练营）

这是一个为期 21 天的 Agent 学习项目，内容以小步、可测试的 Python 练习为主。

这个仓库更适合把它理解成一份“从零开始学习 Agent 系统”的过程记录，而不是一个生产级产品。项目从最基础的输入路由、状态管理开始，逐步扩展到 LangGraph、记忆、评测、配置、日志以及最终的小型毕业项目。

## 项目结构

- `days/`：按天拆分的代码实现，从最小路由、`state`、memory，一直到 LangGraph、LLM tool loop、评测和毕业项目。
- `tests/`：每一天对应的自动化测试。
- `study_notes/`：带读笔记、阶段总结和跟读文件。
- `ARCHITECTURE_GUIDE.md`：项目架构理解指南。
- `FINAL_REVIEW_21_DAYS.md`：21 天总复盘。
- `week1_review.md`、`week2_review.md`：阶段性复盘总结。

## 这个项目在学什么

这个项目的主线不是“背框架 API”，而是先理解一个 Agent 系统最基本的组成，再逐步迁移到更接近真实项目的写法。

整体上可以粗略分成三段：

1. `Day01-Day07`
   手写最小 Agent 骨架，包括输入处理、意图判断、统一 `state`、工具调用、失败处理和统一入口。

2. `Day08-Day14`
   迁移到 LangGraph 风格的图流程，包括节点、边、条件分支、checkpoint 和持久化记忆。

3. `Day15-Day21`
   补上更接近真实系统的部分，包括 LLM adapter、tool loop、HITL、pipeline、评测、配置、日志和毕业项目收口。

## 亮点

- 从最简单的规则路由逐步升级到图式 Agent
- 包含 JSON 和 SQLite 两种状态持久化方式
- 包含 retry、fallback、HITL 和 eval 练习
- 最后收成一个可测试、可演示的小型毕业项目

## 本地运行

建议先进入项目目录，再使用你自己的 Python 环境运行测试：

```bash
pytest tests -q
```

在当前工作区里，这套测试之前已经通过，结果是：

```text
86 passed
```

## 推荐上传到 GitHub 的内容

建议保留：

- `days/`
- `tests/`
- `study_notes/`
- `ARCHITECTURE_GUIDE.md`
- `FINAL_REVIEW_21_DAYS.md`
- `week1_review.md`
- `week2_review.md`
- `.env.example`

建议不要上传：

- `.venv/`
- `.pytest_cache/`
- `__pycache__/`
- `logs/`
- 运行时生成的 `*.sqlite`
- `data/` 或 `days/data/` 下的运行产物 JSON

## 说明

- 当前仓库里可能包含运行过程中产生的数据目录，例如 `data/` 或 `days/data/`。如果你只想保留学习项目本身，这些运行产物可以清理后再上传。
- 部分源码和笔记包含中文内容。如果终端编码不一致，显示上可能会出现乱码，但这不影响 Python 逻辑本身。发布到 GitHub 前，建议统一使用 UTF-8 编码。

## 推荐阅读顺序

如果你是第一次看这个项目，建议不要直接逐行读代码，而是按下面这个顺序理解：

1. 先看 `ARCHITECTURE_GUIDE.md`
2. 再看 `FINAL_REVIEW_21_DAYS.md`
3. 然后看 `study_notes/` 里的带读文件
4. 最后再回到 `days/` 里的具体实现

更适合这个项目的理解方式是：

```python
先看系统架构 -> 再看模块职责 -> 最后再看代码实现
```

## 当前定位

这个仓库目前是：

- 可运行
- 可测试
- 可演示
- 可作为 Agent / LangGraph 学习项目

但它还不是一个面向生产环境的完整 Agent 产品。

如果后续继续扩展，可以往这些方向升级：

- 接入真实 LLM API
- 接入真实 RAG / 检索链路
- 加入 Web API 或前端入口
- 补充更完整的日志、监控和部署方案
