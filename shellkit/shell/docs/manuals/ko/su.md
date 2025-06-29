# su - 사용자 전환 (Linux/macOS 호환)

## 사용법

    su [사용자]


## 설명

현재 `pysh`를 셸 인터프리터로 사용하여, 다른 사용자 계정으로 새로운 **로그인 셸**을 실행합니다.

- **Linux** 에서는 다음과 같은 방식으로 실행됩니다: `su [사용자] -s /path/to/pysh`
- **macOS** 에서는 `sudo /path/to/pysh` 방식으로 대체되며, 인자를 지원하지 않습니다.

이 명령어는 `os.execvp()`를 사용하여 현재 셸 프로세스를 대체하며, 성공 시 복귀하지 않습니다.


## 예시

root 사용자로 전환 (Linux):

```shell
$ su
```

`admin`이라는 사용자로 전환 (Linux):

```shell
$ su admin
```

macOS에서 현재 사용자로 새 셸 시작 (인자 없음):

```shell
$ su
```


## 참고사항

- 이 명령을 사용하려면 `pysh` 바이너리가 `$PATH`에서 검색 가능하거나 직접 실행되어야 합니다.
