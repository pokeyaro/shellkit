# 🐚 Pull Request Checklist for ShellKit

Thanks for contributing to **ShellKit**! Please use this template to guide your pull request and help reviewers understand the context.

---

## 📌 Overview

<!--
Briefly describe what this PR does:
- What command, module, or behavior is changed?
- Why is this needed?
- Is it part of a larger feature roadmap?
-->

## ✅ Type of Change

- [ ] ✨ New Feature
- [ ] 🐛 Bug Fix
- [ ] 📝 Docs Update
- [ ] 🧹 Code Cleanup / Refactor
- [ ] 🧪 Test or Benchmark
- [ ] ⚙️ Dev Tools / CI
- [ ] Other (please specify):

> Summary (optional):

## 🧪 Testing

- [ ] Confirmed CLI usage works (`pysh`)
- [ ] Verified multi-line command execution (if applicable)
- [ ] Traced down to `libc` or `syscall` layer
- [ ] Ran `pytest` with no errors
- [ ] Manually tested on:
  - [ ] macOS
  - [ ] Linux

## 📂 Affected Modules

- [ ] Shell CLI / REPL
- [ ] Built-in commands (`cd`, `echo`, etc.)
- [ ] Libc / syscall emulation
- [ ] Tracing / Debugging tools
- [ ] Localization / i18n
- [ ] Other (specify):

## 📎 Related Issues / Discussions

<!-- e.g. Closes #42, Relates to #7 -->
Closes/Fixes/Related to: #...

---

> 🧠 Tip: Keep PRs focused. Separate unrelated changes into different PRs if possible.
