# arch - 머신 아키텍처 표시

## 사용법

    arch [옵션]


## 설명

현재 머신의 아키텍처를 표시합니다.

- 기본적으로 PySH의 내부 `SYSINFO`에서 값을 가져오며, 이는 플랫폼 간에 통합되어 있습니다.
- `--raw` 옵션을 사용하면 원본 아키텍처 문자열을 위해 시스템의 `arch` 유틸리티를 호출합니다.


## 옵션

- `--raw` 시스템 `arch` 명령어에서 원시 아키텍처 문자열을 가져옵니다.
- `-h, --help` 이 도움말 메시지를 표시합니다.


## 예제

PySH의 내부 SYSINFO에서 정규화된 아키텍처를 표시합니다.

```shell
$ arch
Architecture: x86_64
```

시스템 `arch` 명령어에서 원시 아키텍처 문자열을 가져옵니다.

```shell
$ arch --raw
Architecture (raw): i386
```


## 참고사항

- 내부 아키텍처는 정규화되어 있으며 원시 시스템 결과와 약간 다를 수 있습니다.
- 이 명령어는 Apple Silicon과 Intel Mac을 구분하는 것과 같은 크로스 플랫폼 환경을 구별하는 데 도움이 됩니다.
