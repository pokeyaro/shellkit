"""
docs/texts/help.py

Provides localized help command summaries for the shell.
"""

from shellkit.i18n import I18N_EN, I18N_JA, I18N_KO, I18N_ZH


HELP_TEXT = {
    I18N_EN: """
help (?) - view shell manual pages and built-in command list

\033[1mBuilt-in Commands:\033[0m
  alias                      Show predefined aliases
  arch                       Show machine architecture
  cd [path]                  Change directory
  clear                      Clear the screen
  copyright                  Show copyright notice
  date [--iso]               Show current date and time
  debug [cmd]                Control debug system (reset|status|off|help)
  echo [args...]             Print arguments to stdout
  env [--json]               Show environment variables
  exit / quit [code]         Exit the shell
  export VAR=value           Set environment variables
  help / ? [cmd]             Show help or manual
  history                    Show command history
  license                    Show LICENSE file
  locale [lang|--list]       Show or change current language
  machinfo                   Show detailed machine info
  printf FORMAT [...]        Format output like C's printf
  pwd                        Show current directory
  sleep SECONDS [...]        Pause for a while
  tree [path]                Show directory structure as a tree
  uname [opts]               Show kernel/system info
  which CMD                  Locate a command
  whoami                     Show current user

\033[1mUsage:\033[0m
  `help`                     Show this command list
  `help cd`                  Show help for 'cd'
  `? whoami`                 Equivalent to 'help whoami'

\033[1mTip:\033[0m
  • Help pages are markdown-based manuals with examples and options.
  • For better manual rendering, consider installing tools like: `glow`, `bat`, or `mdcat`.
""",

    I18N_JA: """
help (?) - シェルのマニュアルと組み込みコマンド一覧を表示します

\033[1m組み込みコマンド：\033[0m
  alias                          定義済みのエイリアスを表示
  arch                           マシンのアーキテクチャを表示
  cd [パス]                      カレントディレクトリを変更
  clear                          画面をクリア
  copyright                      著作権情報を表示
  date [--iso]                   現在の日付と時刻を表示
  debug [cmd]                    デバッグ操作（reset|status|off|help）
  echo [引数...]                 引数を出力
  env [--json]                   環境変数を表示
  exit / quit [コード]           シェルを終了
  export 変数=値                 環境変数を設定
  help / ? [コマンド]            ヘルプまたはマニュアルを表示
  history                        コマンド履歴を表示
  license                        LICENSE ファイルを表示
  locale [lang|--list]           言語を表示または変更
  machinfo                       詳細なマシン情報を表示
  printf フォーマット [...]      C風の形式で出力
  pwd                            現在のディレクトリを表示
  sleep 秒数 [...]               一時停止
  tree [パス]                    ディレクトリ構造をツリー表示
  uname [オプション]             カーネル/システム情報を表示
  which CMD                      コマンドの場所を表示
  whoami                         現在のユーザーを表示

\033[1m使い方：\033[0m
  `help`                         コマンド一覧を表示
  `help cd`                      cd コマンドの詳細を見る
  `? whoami`                     'help whoami' と同じ

\033[1mヒント：\033[0m
  • ヘルプは Markdown ベースで、例とオプションを含みます。
  • `glow`、`bat`、`mdcat` などを使うと表示がより快適になります。
""",

    I18N_KO: """
help (?) - 셸 매뉴얼 페이지와 내장 명령어 목록을 봅니다

\033[1m내장 명령어:\033[0m
  alias                      미리 정의된 별칭 표시
  arch                       머신 아키텍처 표시
  cd [경로]                  디렉터리 변경
  clear                      화면 지우기
  copyright                  저작권 공지 표시
  date [--iso]               현재 날짜와 시간 표시
  debug [cmd]                디버그 시스템 제어 (reset|status|off|help)
  echo [인수...]             인수를 표준 출력으로 출력
  env [--json]               환경 변수 표시
  exit / quit [코드]         셸 종료
  export 변수=값             환경 변수 설정
  help / ? [명령어]          도움말 또는 매뉴얼 표시
  history                    명령어 기록 표시
  license                    LICENSE 파일 표시
  locale [언어|--list]       현재 언어 표시 또는 변경
  machinfo                   자세한 머신 정보 표시
  printf 형식 [...]          C의 printf와 같은 형식 출력
  pwd                        현재 디렉터리 표시
  sleep 초 [...]             잠시 일시정지
  tree [경로]                디렉터리 구조를 트리로 표시
  uname [옵션]               커널/시스템 정보 표시
  which CMD                  명령어 위치 찾기
  whoami                     현재 사용자 표시

\033[1m사용법:\033[0m
  `help`                     이 명령어 목록 표시
  `help cd`                  'cd'에 대한 도움말 표시
  `? whoami`                 'help whoami'와 동일

\033[1m팁:\033[0m
  • 도움말 페이지는 예제와 옵션이 포함된 마크다운 기반 매뉴얼입니다.
  • 더 나은 매뉴얼 렌더링을 위해 다음 도구 설치를 고려하세요: `glow`, `bat`, 또는 `mdcat`.
""",

    I18N_ZH: """
help (?) - 查看 shell 帮助文档和内建命令列表

\033[1m内建命令：\033[0m
  alias                       查看预定义别名
  arch                        查看系统架构信息
  cd [路径]                   切换当前目录
  clear                       清屏
  copyright                   显示版权信息
  date [--iso]                显示当前日期和时间
  debug [子命令]              控制调试系统（reset|status|off|help）
  echo [参数...]              将参数输出到终端
  env [--json]                显示环境变量
  exit / quit [退出码]        退出 shell
  export 变量=值              设置环境变量
  help / ? [命令]             显示帮助或文档
  history                     显示历史命令
  license                     显示 LICENSE 文件
  locale [语言|--list]        查看或更改当前语言
  machinfo                    显示详细主机信息
  printf 格式 [...]           类似 C 的 printf 格式化输出
  pwd                         显示当前工作目录
  sleep 秒数 [...]            暂停执行
  tree [路径]                 以树状结构展示目录
  uname [选项]                查看系统内核信息
  which 命令名                查找命令路径
  whoami                      显示当前用户名

\033[1m用法示例：\033[0m
  `help`                      显示命令总览
  `help cd`                   查看 cd 的帮助
  `? whoami`                  等效于 `help whoami`

\033[1m提示：\033[0m
  • 帮助页是基于 markdown 的手册，包含示例与参数说明。
  • 推荐安装：`glow`、`bat` 或 `mdcat`，获得更好的终端阅读体验。
""",
}
