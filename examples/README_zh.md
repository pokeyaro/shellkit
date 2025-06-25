# ShellKit 示例

欢迎来到 ShellKit 示例集！这些 `.log` 文件展示了 ShellKit 功能的真实使用场景，从基础命令到高级调试功能。


## 📖 如何使用这些示例

每个 `.log` 文件包含一个完整的终端会话，展示：
- **用户输入的命令**（在提示符 `pysh [PATH] ➜` 后）
- **ShellKit 的实际输出**
- **你可以跟随操作的交互演示**

直接复制粘贴命令来试试吧！


## 📂 目录结构

### 🟢 `basic/` - 入门指南
非常适合学习 shell 基础的新用户：

- [getting_started.log](./basic/getting_started.log) - 你的第一个 ShellKit 会话
- [help_system.log](./basic/help_system.log) - 掌握内置帮助系统
- [builtin_commands.log](./basic/builtin_commands.log) - 基础命令（pwd、echo、env 等）
- [cd_usage.log](./basic/cd_usage.log) - 目录导航基础
- [history_usage.log](./basic/history_usage.log) - 命令历史和快捷方式

### 🌍 `i18n/` - 多语言支持
探索 ShellKit 的国际化功能：

- [multilingual_demo.log](./i18n/multilingual_demo.log) - 在英语、日语、韩语、中文间切换
- [locale_commands.log](./i18n/locale_commands.log) - 语言环境管理

### 🔍 `inspector/` - 调试与追踪
深入了解 ShellKit 的内省功能：

- [trace_echo_demo.log](./inspector/trace_echo_demo.log) - 追踪 echo/printf 通过 libc 层的调用
- [debug_mode.log](./inspector/debug_mode.log) - 命令解析和执行流程
- [thinking_mode.log](./inspector/thinking_mode.log) - 组合调试 + 追踪分析

### 🚀 `advanced/` - 高级用户功能
面向有经验用户的高级概念：

- [command_line_options.log](./advanced/command_line_options.log) - 所有命令行标志和选项
- [fallback_commands.log](./advanced/fallback_commands.log) - 内置与外部命令机制
- [printf_formatting.log](./advanced/printf_formatting.log) - 完整的 printf 格式说明符
- [special_variables.log](./advanced/special_variables.log) - Shell 变量（$$、$?、$0）
- [tab_auto_completion.log](./advanced/tab_auto_completion.log) - 智能 Tab 补全


## 🎯 快速开始指南

1. **Shell 新手？** 从 [`basic/getting_started.log`](basic/getting_started.log) 开始
2. **想看多语言魔法？** 查看 [`i18n/multilingual_demo.log`](i18n/multilingual_demo.log)
3. **对内部机制好奇？** 试试 [`inspector/trace_echo_demo.log`](inspector/trace_echo_demo.log)
4. **准备好高级功能？** 探索 [`advanced/printf_formatting.log`](advanced/printf_formatting.log)


## 💡 学习提示

- **跟随操作**：边读边输入命令
- **大胆实验**：修改示例看看会发生什么
- **使用帮助**：记住用 `help <命令>` 查看详细文档
- **忽略大小写**：Tab 补全不区分大小写
- **多语言**：试试 `export PYSH_LANG=zh` 切换到中文界面


## 🔧 入门示例命令

```bash
# 基础用法
$ pysh
echo "你好，ShellKit！"
help echo
exit

# 带选项
$ pysh --no-banner --prompt-color green
$ pysh -c "printf '快速测试: %s\n' '成功'"
$ pysh --trace-echo

# 多语言
$ export PYSH_LANG=zh && pysh
```


## 🎨 想要一个彩色的提示符主题？

```bash
$ pysh
export PS1="\033[90m[\033[1;32mdemo\033[90m@\033[31mm\033[33ma\033[32mc\033[36mb\033[34mo\033[35mo\033[31mk\033[33mp\033[32mr\033[34mo\033[90m ~]\033[90m$ \033[0m"
[demo@macbookpro ~]$ 
```
![img.png](assets/img.png)


## 📚 相关文档

- **安装说明**：查看主 `README.md`
- **命令参考**：在 ShellKit 中使用 `help`
- **开发文档**：查看 `docs/` 目录
- **贡献指南**：查看 `CONTRIBUTING.md`


## 🌟 这些示例的特色

- **真实终端会话** - 非人造示例
- **渐进复杂度** - 从初学者到专家
- **跨平台** - 在 macOS、Linux 和 Windows 上都能运行
- **教育导向** - 学习 shell 概念和系统调用
- **多语言** - 4 种语言的示例（中/英/日/韩）

---

**准备好探索了吗？** 选择适合你经验水平的目录开始吧！

*记住：ShellKit 是为学习而设计的。不要害怕实验和搞坏东西——这正是学习的最佳方式！* 🚀

---

← [返回主页](../README_zh.md)
