# Day 02 学习笔记：猜数字游戏与异常处理

## 1. 今日成就
我今天完成了一个带防弹衣（异常处理）的猜数字游戏，并学会了使用 VS Code 和 Markdown。

## 2. 核心知识点
- **input()**：接收用户输入，但默认是字符串。
- **int()**：把字符串转成整数，如果传入字母会报错。
- **try...except ValueError**：捕获输入错误，防止程序崩溃。

## 3. 踩坑记录
报错：`TabError: inconsistent use of tabs and spaces in indentation`
> 原因：Python 对缩进极其严格，混用了 Tab 键和空格键。
> 解决：全部统一用 4 个空格。

## 4. 代码片段
```python
try:
    guess = int(guess)
except ValueError:
    print("❌ 输入错误！请输入整数！")
    continue