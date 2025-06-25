# alias - 명령어 별칭 정의 또는 표시

## 사용법

    alias
    alias 이름
    alias 이름='명령어'


## 설명

셸 명령어 별칭을 생성하거나 표시합니다.

- 인수 없이 `alias`를 실행하면 정의된 모든 별칭을 나열합니다.
- `이름` 하나만 지정하면 해당 별칭 정의를 보여줍니다.
- `이름='명령어'` 쌍으로 지정하면 새로운 별칭을 정의합니다.

별칭은 자주 사용하는 명령어의 단축키 역할을 합니다.


## 예제

새 별칭 정의하기:

```shell
$ alias greet='echo Hello World'
$ greet
Hello World
```

특정 별칭 조회하기:

```shell
$ alias greet
greet='echo Hello World'
```

모든 별칭 나열하기:

```shell
$ alias
ll='ls -l'
la='ls -a'
greet='echo Hello World'
```

이러한 별칭은 자주 사용하는 명령어의 편의성을 향상시킵니다.


## 참고사항

- 별칭은 **읽기 전용**이며 현재 **하드코딩**되어 있습니다.
- 별칭이 어떤 명령어로 확장되는지 보려면 다음을 사용하세요:

```shell
$ which greet
greet: alias for 'echo Hello World'
```
