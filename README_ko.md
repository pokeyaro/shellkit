# 🐚 ShellKit (libc + pysh)

> `echo`가 어떻게 동작하는지, 셸에서 시스템 콜까지 Python으로 단계별 추적.

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org)
[![PyPI version](https://img.shields.io/pypi/v/shellkit)](https://pypi.org/project/shellkit/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)](https://github.com/pokeyaro/shellkit)
[![Languages](https://img.shields.io/badge/languages-EN%20%7C%20中文%20%7C%20日本語%20%7C%20한국어-brightgreen)](./examples/)
[![CI](https://github.com/pokeyaro/shellkit/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/pokeyaro/shellkit/actions/workflows/ci.yml)

[English](./README.md) | [简体中文](./README_zh.md) | [日本語](./README_ja.md) | **한국어**

---

## 📖 개요

`ShellKit`은 Unix 스타일의 교육용 터미널 툴킷으로, 두 개의 하위 프로젝트로 구성됩니다:

* **Libc**: Python으로 구현한 C 라이브러리 시뮬레이션. `syscall`, `write`, `printf` 등을 포함하며, 유저 모드에서 커널 모드로의 흐름을 시각화합니다.
* **Pysh**: `Libc` 위에 구축된 대화형 셸. 내부 명령어, REPL, 계층간 추적 기능과 다국어 지원을 제공합니다. 시스템 프로그래머와 터미널 마니아를 위한 도구입니다.

macOS와 Linux에서 사용 가능하며, Arm64 및 x86\_64 아키텍처를 지원합니다.


## ✨ 기능

### Pysh

* 🧠 내장 명령어 (`cd`, `echo`, `pwd`, `env` 등)
* 🧵 다국어 지원 (영/중/일/한 매뉴얼 제공)
* 🔍 계층 간 트레이싱 (명령 파싱 → libc 함수 → C syscall)
* 🧩 조합 가능한 REPL 실행 모델
* 🔌 플러그인 기반 명령 등록 시스템

### Libc

* 🖨️ 커스텀 `printf` 엔진 (`%s`, `%d`, `%f` 및 이스케이프 시퀀스 지원)
* 📜 Python ↔ C `syscall` 브릿지 (`syscall/syslib.so` 사용)
* 🧪 `pytest` 테스트 포함, 핵심 함수 성능 벤치마크 제공


## 📦 설치 방법

> Python 3.10 이상 필요

pip로 설치:

```bash
pip install shellkit
```

설치 후 다음 명령으로 실행:

```bash
pysh
```


## 🚀 사용법

```bash
pysh [옵션들]
```

### 명령줄 옵션

| 옵션              | 설명                              |
| --------------- | ------------------------------- |
| `--command`     | 단일 명령 실행                        |
| `--no-banner`   | 시작 배너 출력 생략                     |
| `--no-reminder` | 휴식 알림 비활성화                      |
| `--quiet`       | 조용한 모드 (최소 출력)                  |
| `--safe`        | 안전 모드 (`rm -rf /` 등의 위험 명령 차단)  |
| `--debug`       | 셸 명령 디버깅 정보 표시                  |
| `--trace-echo`  | `echo`, `printf`의 libc 호출 경로 추적 |

도움말 보기:

```bash
pysh --help
```


## 📚 예제 및 튜토리얼

ShellKit의 실제 동작을 보고 싶으신가요? 포괄적인 예제들을 확인해보세요:

→ **[예제 및 데모](./examples/README_ko.md)** - 기본부터 고급 기능까지, 실제 터미널 세션

*다국어 데모, 디버깅 튜토리얼, 고급 printf 포매팅이 포함되어 있습니다!*


## 📦 프로젝트 구조 (일부)

```

shellkit/
├── native/         # C로 작성된 syscall 구현
├── shellkit/       # 메인 패키지
│   ├── syscall/    # Python에서 호출하는 ctypes 기반 래퍼
│   ├── libc/       # 커스텀 libc (printf, write, exit 등)
│   ├── shell/      # 핵심 엔진, 내장 명령어, REPL 실행기
│   ├── inspector/  # 디버그 및 트레이싱 도구
│   └── i18n/       # 다국어 지원 및 번역 모듈
├── benchmarks/     # 성능 벤치마크
├── examples/       # 사용 예제 및 데모 로그
└── tests/          # 테스트 스위트
```


## 🧩 지원 플랫폼 (syslib.so)

| 플랫폼                        | 지원 여부 | 설명                                   |
| -------------------------- | ----- | ------------------------------------ |
| **Linux x86\_64**          | ✅ 지원  | `rax = 1` + `syscall` 방식             |
| **Linux ARM64**            | ✅ 지원  | `x8 = 64` + `svc #0` 방식              |
| **macOS Intel (x86)**      | ✅ 지원  | `rax = 0x2000004` + `syscall` 방식     |
| **macOS ARM64 (M1/M2/M3)** | ✅ 지원  | `syscall(SYS_write, ...)` 방식으로 래핑 처리 |
| **Windows**                | ❌ 미지원 | Windows는 `syscall()` 인터페이스가 없음       |


## 📌 변경 내역

자세한 내용은 [CHANGELOG.md](./CHANGELOG.md) 참고.


## 📜 라이선스

MIT 라이선스. 자세한 내용은 [LICENSE](./LICENSE)를 확인하세요.


## 🤝 감사의 말

고전 Unix Shell의 철학에 영감을 받아 개발. \
모든 시스템 프로그래머들과 터미널 애호가 여러분께 감사드립니다.
