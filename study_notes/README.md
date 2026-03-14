# 代码带读笔记

这个目录存放按天整理的“详细带读版”学习笔记。

现在代码目录已经改成了：

```text
agent-bootcamp/
  days/
    day01/
    day02/
    ...
  tests/
  study_notes/
```

所以你后面看代码时，建议统一按这个顺序：

1. 先看 `days/dayXX` 里的代码文件
2. 再看这里对应的 `dayXX_reading.md`
3. 最后看 `tests/test_dayXX_*.py`

## 推荐阅读顺序

### 第一周：手写版 Agent 基础

1. `day01_reading.md`
2. `day02_reading.md`
3. `day03_reading.md`
4. `day04_reading.md`
5. `day05_reading.md`
6. `day06_reading.md`
7. `day07_reading.md`

### 第二周：LangGraph 与状态流转

8. `day08_reading.md`
9. `day09_reading.md`
10. `day10_reading.md`
11. `day11_reading.md`
12. `day12_reading.md`
13. `day13_reading.md`
14. `day14_reading.md`

### 第三周：模型、工具、流程扩展

15. `day15_reading.md`
16. `day16_reading.md`
17. `day17_reading.md`
18. `day18_reading.md`
19. `day19_reading.md`

## 你阅读时最该抓的线

不要把每天看成完全独立的题目，  
更好的方式是一直抓住这条主线：

```python
用户输入
-> state
-> 路由 / 节点 / 工具
-> 中间结果更新
-> 回复
-> 记忆 / 恢复 / 错误处理
-> 评测
```

这条线抓住了，后面看到 LangGraph、checkpointer、tool calling、HITL 都不会乱。
