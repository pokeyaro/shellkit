# ShellKit Examples

Welcome to the ShellKit examples! These `.log` files demonstrate real-world usage scenarios of ShellKit's features, from basic commands to advanced debugging capabilities.


## 📖 How to Use These Examples

Each `.log` file contains a complete terminal session showing:
- **Commands typed by users** (after the prompt `pysh [PATH] ➜`)
- **Actual output** from ShellKit
- **Interactive demonstrations** you can follow along

Simply copy and paste the commands to try them yourself!


## 📂 Directory Structure

### 🟢 `basic/` - Getting Started
Perfect for new users learning shell basics:

- [getting_started.log](./basic/getting_started.log) - Your first ShellKit session
- [help_system.log](./basic/help_system.log) - Master the built-in help system  
- [builtin_commands.log](./basic/builtin_commands.log) - Essential commands (pwd, echo, env, etc.)
- [cd_usage.log](./basic/cd_usage.log) - Directory navigation fundamentals
- [history_usage.log](./basic/history_usage.log) - Command history and shortcuts

### 🌍 `i18n/` - Multilingual Support
Explore ShellKit's international features:

- [multilingual_demo.log](./i18n/multilingual_demo.log) - Switch between English, Japanese, Korean, Chinese
- [locale_commands.log](./i18n/locale_commands.log) - Language environment management

### 🔍 `inspector/` - Debugging & Tracing
Deep dive into ShellKit's introspection capabilities:

- [trace_echo_demo.log](./inspector/trace_echo_demo.log) - Trace echo/printf through libc layer
- [debug_mode.log](./inspector/debug_mode.log) - Command parsing and execution flow
- [thinking_mode.log](./inspector/thinking_mode.log) - Combined debug + trace analysis

### 🚀 `advanced/` - Power User Features
Advanced concepts for experienced users:

- [command_line_options.log](./advanced/command_line_options.log) - All command-line flags and options
- [fallback_commands.log](./advanced/fallback_commands.log) - Built-in vs external command mechanism
- [printf_formatting.log](./advanced/printf_formatting.log) - Complete printf format specifiers
- [special_variables.log](./advanced/special_variables.log) - Shell variables ($$, $?, $0)
- [tab_auto_completion.log](./advanced/tab_auto_completion.log) - Intelligent tab completion


## 🎯 Quick Start Guide

1. **New to shells?** Start with [`basic/getting_started.log`](basic/getting_started.log)
2. **Want to see the multilingual magic?** Check [`i18n/multilingual_demo.log`](i18n/multilingual_demo.log)
3. **Curious about the internals?** Try [`inspector/trace_echo_demo.log`](inspector/trace_echo_demo.log)
4. **Ready for advanced features?** Explore [`advanced/printf_formatting.log`](advanced/printf_formatting.log)


## 💡 Tips for Learning

- **Follow along**: Type the commands as you read
- **Experiment**: Modify the examples to see what happens
- **Use help**: Remember `help <command>` for detailed documentation
- **Case-insensitive**: Tab completion ignores case differences
- **Multi-language**: Try `export PYSH_LANG=ja` for Japanese interface


## 🔧 Example Commands to Get Started

```bash
# Basic usage
$ pysh
echo "Hello, ShellKit!"
help echo
exit

# With options
$ pysh --no-banner --prompt-color green
$ pysh -c "printf 'Quick test: %s\n' 'success'"
$ pysh --trace-echo

# Multilingual
$ export PYSH_LANG=en && pysh
```


## 🎨 Want a colorful prompt theme?

```bash
$ pysh
export PS1="\033[90m[\033[1;32mdemo\033[90m@\033[31mm\033[33ma\033[32mc\033[36mb\033[34mo\033[35mo\033[31mk\033[33mp\033[32mr\033[34mo\033[90m ~]\033[90m$ \033[0m"
[demo@macbookpro ~]$ 
```
![img.png](assets/img.png)


## 📚 Related Documentation

- **Installation**: See main `README.md`
- **Command Reference**: Use `help` within ShellKit
- **Development**: Check `docs/` directory
- **Contributing**: See `CONTRIBUTING.md`


## 🌟 What Makes These Examples Special

- **Real terminal sessions** - No artificial examples
- **Progressive complexity** - From beginner to expert
- **Cross-platform** - Works on macOS, Linux, and Windows
- **Educational focus** - Learn shell concepts and system calls
- **Multilingual** - Examples in 4 languages (en/ja/ko/zh)

---

**Ready to explore?** Pick a directory that matches your experience level and dive in! 

*Remember: ShellKit is designed for learning. Don't hesitate to experiment and break things - that's how you learn best!* 🚀

---

← [Back to Main](../README.md)
