# cpplineTest

[English](#english) | [中文](#中文)

## 中文

### 这是什么？
这是一个极其简单的 Python 脚本，存在的唯一目的就是生成一个行数惊人的 C++ 源文件。目前配置下，它会生成一个包含 2,000,000（两百万）行代码的 `.cpp` 文件。

### 为什么要这么做？
1. 测试你的 IDE 或者文本编辑器在打开巨型文件时会不会直接崩溃。
2. 测试 Git 在处理接近 100MB 限制的单文件时的极限。
3. 让你的代码统计图表看起来像个天才，或者像个疯子。
4. 纯粹因为我们可以。

### 核心参数
* 目标行数：2,000,000 行
* 文件大小：约 71MB（刚好躲过 GitHub 的 100MB 封杀令，但会触发 50MB 的警告）
* 语法：包含模板类、Lambda 表达式、结构体和命名空间。它可以通过语法检查，但如果你真的尝试编译它，请确保你的内存条足够粗。

### 快速开始
确保你安装了 Python 3.12（其实 3.x 应该都能跑）：
```bash
python3 main.py
```

### 参与贡献
如果你觉得现在的代码生成模式太单调了，或者你有办法在不增加文件体积的前提下塞进更多奇怪的 C++ 特性，欢迎直接提交 PR。只要别把 GitHub 的服务器搞炸，一切好说。

---

## English

### What is this?
A dead-simple Python script whose sole purpose in life is to manifest a C++ source file of absurd proportions. In its current state, it cranks out a `.cpp` file with 2,000,000 (two million) lines of code.

### Why on earth?
1. To see if your IDE or text editor gives up on life when opening a massive file.
2. To test the boundaries of Git and GitHub when pushing files near the 100MB hard limit.
3. To make your contribution stats look like you are either a god or a maniac.
4. Purely because the "New File" button wasn't enough.

### The Stats
* Target Lines: 2,000,000
* File Size: ~71MB (Sneaks under GitHub's 100MB hard limit, but triggers the "too big" warning).
* Syntax: Features template classes, lambdas, structs, and namespaces. It's technically valid C++, but don't try to compile it unless you have RAM to burn.

### Quick Start
Make sure you have Python 3.12 (though any 3.x should do):
```bash
python3 main.py
```

### Contributing
If you think the current code generation is too boring, or if you know a way to cram even more cursed C++ features into the file without blowing past the 100MB limit, feel free to open a PR. As long as we don't accidentally sentient the GitHub servers, we're good.
