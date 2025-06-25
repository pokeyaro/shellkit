# echo - 변수 치환과 이스케이프 지원으로 텍스트 출력

## 사용법

    echo [-n] [텍스트...]


## 설명

다음 기능을 지원하여 주어진 텍스트를 표준 출력으로 출력합니다:

- 환경 변수 치환 (`$VAR`, `${VAR}`)
- 이스케이프된 변수는 리터럴로 보존됩니다 (`\$VAR`, `\${VAR}`)
- `\n`, `\t`와 같은 표준 이스케이프 시퀀스
- `-n` 옵션으로 끝의 개행 문자를 비활성화합니다


## 기능

- `$VAR`와 `${VAR}`는 현재 셸 환경을 사용하여 치환됩니다.
- 리터럴 변수(예: `$USER`)를 표시하려면 달러 기호를 이스케이프하세요: `\$USER`.
- 일반적인 이스케이프 시퀀스(`\n`, `\t` 등)가 해석됩니다.
- `-n`은 출력 끝의 자동 개행을 방지합니다.


## 예제

개행이 포함된 줄 출력:

```shell
$ echo "Hello\nWorld"
Hello
World
$ 
```

개행 없이 줄 출력:

```shell
$ echo -n "Hello, World"
Hello, World $ 
```

변수 치환:

```shell
$ export GREETING="World"
$ echo "Hello, $GREETING"
Hello, World
$ 
```

치환을 방지하기 위해 변수 이스케이프:

```shell
$ echo "Hello, \$GREETING"
Hello, $GREETING
$ 
```


## 참고사항

- 변수 값은 현재 셸 환경(`$USER`, `$HOME` 등)에서 가져옵니다.
- echo하기 전에 환경 변수를 설정하려면 `export`를 사용하세요.
- 백슬래시 이스케이프는 Python 스타일 디코딩을 사용합니다: `\n`, `\t`, `\\` 등.
