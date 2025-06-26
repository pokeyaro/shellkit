# tree - 시스템 `tree` 명령어를 사용하여 디렉터리 구조 표시

## 사용법

    tree [경로] [옵션]


## 설명

트리 형태의 형식으로 재귀적 디렉터리 목록을 표시합니다.

- 이 명령어는 시스템에 설치된 `tree` 유틸리티의 래퍼입니다.
- 기본적으로 일반적으로 무시되는 디렉터리(예: `.git`, `__pycache__`, `.venv`)는 재정의되지 않는 한 제외됩니다.
- 모든 추가 인수는 기본 `tree` 바이너리에 직접 전달됩니다.


## 기본 무시 디렉터리

다음 디렉터리들이 기본적으로 제외됩니다:

- `.git`, `.hg`, `.svn`
- `.idea`, `.vscode`, `.DS_Store`
- `__pycache__`, `.mypy_cache`, `.pytest_cache`, `.tox`
- `.coverage`, `htmlcov`, `coverage.xml`
- `.venv`, `venv`, `env`
- `node_modules`
- `.trash`, `Thumbs.db`, `desktop.ini`


## 예제

현재 디렉터리의 트리를 표시합니다.

```shell
$ tree
```

숨겨진 파일을 포함한 전체 트리와 요약 보고서를 표시합니다.

```shell
$ tree -v
```

파일 크기와 함께 2단계 깊이까지 표시합니다.

```shell
$ tree -L 2 -s
```

기본값 외에 추가 디렉터리를 제외하려면 고유한 값과 함께 `-I`를 사용합니다. 예를 들어:

```shell
$ tree -I "target"
```


## 참고사항

- 이 명령어는 시스템 `tree` 바이너리가 `$PATH`에서 사용 가능해야 합니다.
- 누락된 경우 셸이 설치 방법을 제안합니다:

  - macOS: `brew install tree`
  - Ubuntu/Debian: `sudo apt install tree`

- `tree` 호출 중 발생한 모든 오류는 stderr로 보고됩니다.
