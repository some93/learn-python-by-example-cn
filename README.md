# 🎓 Python by Example · 师兄带你学

> 一份写给纯小白的 Python 入门到进阶教程。内容改编自[廖雪峰的 Python 教程](https://liaoxuefeng.com/books/python/)，**63 关全部用「师兄带你学」的风格原创重写讲解** 🎉

## 🍜 这是个什么项目？

如果你是编程小白，或者从别的语言转过来想快速上手 Python，这个仓库就是为你准备的。

咱们把廖雪峰 Python 教程的**核心知识点拆成 63 个独立小关卡**，每一个都像学长坐在你旁边一样重新讲了一遍 —— 带生活化类比、带踩坑故事、带吐槽感，但也保住了专业性。只要你跟着一关一关走，就能从 `Hello World` 一路学到异步 IO。

**每一关都包含：**
- 📄 完整可运行的 `.py` 源码（带中文注释，复制就能跑）
- 🎯 一句话说清这一关解决什么问题
- 🤔 一个生活化的小问题引入概念（奶茶店、外卖、快递柜、宿舍……）
- 📖 看代码（完整源码）
- 🔍 师兄给你逐行拆代码（核心讲解）
- 🏃 跑一下试试（命令 + 预期输出）
- 💡 师兄的碎碎念（踩坑提醒 + 冷知识）
- 🎓 知识点清单（面试 / 复习用）
- ➡️ 下一关（顺着链接一路学下去）

## 🗺️ 63 关学习路线

### 🌱 第一章 · 入门基础（第 01–15 关）

从 Hello World 开始，搞定 Python 的数据类型、控制结构、函数定义和切片操作。

- [第 01 关 · Hello World](./01-hello-world/)
- [第 02 关 · 数据类型和变量](./02-values/)
- [第 03 关 · 字符串和编码](./03-strings/)
- [第 04 关 · 列表 List](./04-lists/)
- [第 05 关 · 元组 Tuple](./05-tuples/)
- [第 06 关 · 条件判断](./06-if-else/)
- [第 07 关 · 模式匹配](./07-pattern-matching/)
- [第 08 关 · 循环](./08-loops/)
- [第 09 关 · 字典 Dict](./09-dicts/)
- [第 10 关 · 集合 Set](./10-sets/)
- [第 11 关 · 调用函数](./11-calling-functions/)
- [第 12 关 · 定义函数](./12-defining-functions/)
- [第 13 关 · 函数的参数](./13-function-parameters/)
- [第 14 关 · 递归函数](./14-recursion/)
- [第 15 关 · 切片](./15-slicing/)

### 🚀 第二章 · 进阶特性（第 16–19 关）

迭代、列表生成式、生成器、迭代器 —— Python 最优雅的四件武器。

- [第 16 关 · 迭代](./16-iteration/)
- [第 17 关 · 列表生成式](./17-list-comprehensions/)
- [第 18 关 · 生成器](./18-generators/)
- [第 19 关 · 迭代器](./19-iterators/)

### ⚡ 第三章 · 函数式编程（第 20–26 关）

高阶函数、闭包、装饰器、偏函数 —— 写出更简洁、更 Pythonic 的代码。

- [第 20 关 · map/reduce](./20-map-reduce/)
- [第 21 关 · filter](./21-filter/)
- [第 22 关 · sorted](./22-sorted/)
- [第 23 关 · 返回函数（闭包）](./23-closures/)
- [第 24 关 · 匿名函数](./24-lambda/)
- [第 25 关 · 装饰器](./25-decorators/)
- [第 26 关 · 偏函数](./26-partial-functions/)

### 📦 第四章 · 模块（第 27–28 关）

用模块组织代码，用 pip 安装第三方库。

- [第 27 关 · 模块](./27-modules/)
- [第 28 关 · 安装第三方模块](./28-install-modules/)

### 🏗️ 第五章 · 面向对象编程（第 29–39 关）

类和实例、继承多态、魔法方法、枚举、元类 —— Python OOP 的完整体系。

- [第 29 关 · 类和实例](./29-classes-and-instances/)
- [第 30 关 · 访问限制](./30-access-restriction/)
- [第 31 关 · 继承和多态](./31-inheritance/)
- [第 32 关 · 获取对象信息](./32-object-info/)
- [第 33 关 · 实例属性和类属性](./33-instance-class-attrs/)
- [第 34 关 · \_\_slots\_\_](./34-slots/)
- [第 35 关 · @property](./35-property/)
- [第 36 关 · 多重继承](./36-multiple-inheritance/)
- [第 37 关 · 定制类](./37-custom-classes/)
- [第 38 关 · 枚举类](./38-enum/)
- [第 39 关 · 元类](./39-metaclass/)

### 🛡️ 第六章 · 错误、调试与测试（第 40–42 关）

异常处理、调试技巧、单元测试 —— 写出健壮的代码。

- [第 40 关 · 错误处理](./40-error-handling/)
- [第 41 关 · 调试](./41-debugging/)
- [第 42 关 · 单元测试](./42-unit-testing/)

### 💾 第七章 · IO 编程（第 43–46 关）

文件读写、内存 IO、目录操作、序列化 —— 让程序和外部世界打交道。

- [第 43 关 · 文件读写](./43-file-io/)
- [第 44 关 · StringIO 和 BytesIO](./44-stringio-bytesio/)
- [第 45 关 · 操作文件和目录](./45-os-operations/)
- [第 46 关 · 序列化](./46-serialization/)

### 🔧 第八章 · 进程、线程与正则（第 47–50 关）

多进程、多线程、ThreadLocal、正则表达式 —— 性能优化和文本处理的利器。

- [第 47 关 · 多进程](./47-multiprocessing/)
- [第 48 关 · 多线程](./48-multithreading/)
- [第 49 关 · ThreadLocal](./49-threadlocal/)
- [第 50 关 · 正则表达式](./50-regex/)

### 🌐 第九章 · 常用模块与网络编程（第 51–63 关）

内建模块、第三方库、网络编程、数据库、Web 开发、异步 IO —— 从工具箱到实战。

- [第 51 关 · datetime](./51-datetime/)
- [第 52 关 · collections](./52-collections/)
- [第 53 关 · base64](./53-base64/)
- [第 54 关 · hashlib](./54-hashlib/)
- [第 55 关 · itertools](./55-itertools/)
- [第 56 关 · contextlib](./56-contextlib/)
- [第 57 关 · requests](./57-requests/)
- [第 58 关 · TCP 编程](./58-tcp-programming/)
- [第 59 关 · UDP 编程](./59-udp-programming/)
- [第 60 关 · 使用 SQLite](./60-database-sqlite/)
- [第 61 关 · WSGI 接口](./61-wsgi/)
- [第 62 关 · 使用 Web 框架](./62-web-framework/)
- [第 63 关 · 异步 IO](./63-async-io/)

## 🚀 怎么用这个仓库

1. **装 Python**：前往 [python.org](https://www.python.org/downloads/)，安装 Python 3.10+（推荐 3.12）。
2. **Clone 仓库**：
   ```bash
   git clone https://github.com/your-username/learn-python-by-example-cn.git
   cd learn-python-by-example-cn
   ```
3. **进任意一关的文件夹跑代码**：
   ```bash
   cd 01-hello-world
   python hello-world.py
   ```
4. **打开同目录的 `README.md`**，跟着师兄的节奏学。

### 📌 推荐学习节奏

- **一天 2–3 关**，一个月内能通关；
- **别囫囵吞枣** —— 每关的「💡 师兄的碎碎念」部分通常比代码本身更值钱，那里藏着大量踩坑提醒；
- **按顺序学**最好，面向对象那几关强烈依赖前面的基础；
- **动手跑**每一个例子，不要只看不跑；
- 后面几关（Web 框架、requests 等）需要安装第三方库，建议先看[第 28 关](./28-install-modules/)学会用 venv + pip。

## 🙏 致谢

这个仓库站在巨人的肩膀上：

- **原教程**：[廖雪峰的 Python 教程](https://liaoxuefeng.com/books/python/) —— 中文世界最经典的 Python 入门教程之一。
- **姊妹项目**：[learn-go-by-example-cn](https://github.com/CXP-shawn/learn-go-by-example-cn) —— 同风格的 Go 语言教程，79 关通关。

**教程的知识体系和内容编排参考了廖雪峰的 Python 教程**，本仓库在此基础上进行了**「师兄带你学」风格的原创重写**，所有讲解文字和代码示例均为原创。

如果你觉得这个项目对你有帮助，顺手点个 Star 🌟 支持一下。

## 📬 反馈 & 贡献

- 发现讲解有误、有更好的类比、或者觉得哪一节太生硬？**欢迎开 Issue**；
- 想补充更多关卡（比如 Django、爬虫、数据分析）？**欢迎 PR**；
- 觉得风格还行，**欢迎 Star + 转发给身边正在学 Python 的同学**。

## 📜 License

MIT License — 使用自由，但请保留致谢部分。

---

🎉 **63 关全部通关，祝你学得愉快！**
