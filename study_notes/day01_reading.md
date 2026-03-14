# Day01 代码带读

对应代码文件：`days/day01/router.py`  
对应测试文件：`tests/test_day01_router.py`

## 1. 今天的目标是什么

Day01 的目标非常小，但它是后面所有内容的起点：

```python
先把用户输入变成一个最小、可判断的意图结果
```

你可以把它理解成：

```python
用户说了一句话
-> 系统先别急着做事
-> 先判断这句话大概属于哪一类
```

这一天只做最简单的三分类：

- `weather`
- `math`
- `unknown`

## 2. 整体架构

文件里有 3 个函数：

1. `normalize_text`
2. `detect_intent`
3. `route`

它们的关系是：

```python
route()
  -> detect_intent()
      -> normalize_text()
```

也就是说：

- 最底层先清洗输入
- 中间层再判断意图
- 最外层最后返回统一结构

## 3. `normalize_text` 在做什么

函数签名：

```python
def normalize_text(text: str) -> str:
```

这个函数不是在“理解”用户，  
它只是先做输入清洗。

核心动作有 4 个：

1. 判断输入必须是字符串
2. 去掉首尾空格
3. 转成小写
4. 如果清洗后为空，直接报错

比如：

```python
"  Weather In Beijing  " -> "weather in beijing"
```

这一步的意义是：

```python
先把输入整理成稳定格式，后面判断才不容易乱
```

## 4. `detect_intent` 在做什么

函数签名：

```python
def detect_intent(text: str) -> str:
```

它先调用：

```python
normalized = normalize_text(text)
```

然后根据关键词判断是哪一类意图。

天气类关键字：

```python
weather / temperature / forecast
```

数学类关键字或运算符：

```python
+ - * / math / calc
```

都不命中时返回：

```python
unknown
```

这里你要建立一个很重要的感觉：

```python
意图识别不一定要很复杂
最开始可以只是“规则 + 关键词”
```

## 5. `route` 在做什么

函数签名：

```python
def route(text: str) -> dict:
```

它的工作很简单：

```python
return {"intent": detect_intent(text)}
```

也就是说，`route()` 是对外入口，  
它把内部判断结果包成一个统一字典。

这一步虽然看起来很小，但非常重要，  
因为从 Day01 开始你就在养成一个习惯：

```python
尽量统一返回结构
```

而不是一会儿返回字符串，一会儿返回列表，一会儿返回异常对象。

## 6. 测试怎么读

测试文件里主要验证 4 件事：

1. 天气输入是否被识别成 `weather`
2. 数学输入是否被识别成 `math`
3. 普通文本是否走 `unknown`
4. 空输入是否报错

你可以把测试当成“功能说明书”。

## 7. 这一天真正要记什么

不要背每一行代码，  
只记这条线：

```python
normalize_text -> detect_intent -> route
```

翻成中文就是：

```python
先清洗输入 -> 再判断意图 -> 最后统一输出
```

这就是 Day01 的全部核心。
