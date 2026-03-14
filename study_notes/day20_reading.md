# Day20 代码带读

对应代码文件：`days/day20/config.py`  
对应代码文件：`days/day20/logging_setup.py`  
对应环境样例：`.env.example`  
对应测试文件：`tests/test_day20_config.py`

## 1. 今天的目标是什么

Day20 的主题不是再加一个 Agent 能力，  
而是让项目更像一个可交付项目。

也就是：

```python
配置更明确
日志更统一
新机器更容易启动
```

## 2. 核心文件

1. `config.py`
2. `logging_setup.py`
3. `.env.example`

## 3. `load_settings`

它负责从环境变量读取配置。

当前最小配置包括：

- `APP_ENV`
- `LOG_LEVEL`
- `DEFAULT_THREAD_ID`

这一步的意义是：

```python
不要把配置写死在代码里
```

## 4. `validate_settings`

它负责校验配置是否合法。

例如：

- `app_env` 只能是 `dev / test / prod`
- `log_level` 必须是合法日志级别
- `default_thread_id` 不能是空值

这一步的意义是：

```python
配置错了要尽早失败，不要拖到运行中间才炸
```

## 5. `setup_logging`

它负责做最小日志初始化。

你现在不用把它想复杂，  
它只是先让项目统一用一个 logger 名字和统一格式输出。

## 6. `.env.example`

这个文件的意义不是程序逻辑，  
而是告诉别人：

```python
这个项目运行前至少要准备哪些环境变量
```

## 7. 为什么 Day20 很重要

因为到这一步，如果代码只能在你自己机器上凭感觉跑，  
那还不算“工程化”。

Day20 学的是：

```python
让别人也更容易把它跑起来
```

## 8. 这一天真正要记什么

Day20 的一句话：

```python
能跑和可交付不是一回事，配置和日志是工程化基础
```
