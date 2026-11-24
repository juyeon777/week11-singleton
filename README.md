# 11주차 실습 – Singleton 패턴 (Python)

## 1. 선택 언어 및 실행 환경

| 항목 | 내용 |
| --- | --- |
| 언어 | Python |
| 버전 | Python 3.13.12 (Python 3.8 이상이면 실행 가능) |
| OS | macOS (Darwin 24.6.0) |
| 외부 라이브러리 | 없음 (표준 라이브러리만 사용) |

## 2. 프로젝트 구조

```
.
├── README.md
└── src
    ├── singleton.py   # Singleton 클래스(AppConfig) 구현
    └── main.py        # 동일 인스턴스 비교 · 상태 공유 확인용 실행 코드
```

## 3. 실행 방법

```bash
git clone https://github.com/juyeon777/week11-singleton.git
cd week11-singleton
python3 src/main.py
```

## 4. 구현 요약

- `AppConfig._instance` : 유일한 인스턴스를 보관하는 클래스 변수
- `AppConfig.get_instance()` : `_instance`가 비어 있을 때만 객체를 만들고, 이후에는 같은 객체를 반환
- `__new__` 재정의 : `AppConfig()`처럼 생성자를 직접 호출하면 `TypeError`를 발생시켜 임의 생성을 막음
- 상태 : `counter`(카운터), `theme`(설정 값)

## 5. 실행 결과

```
=== 1. 동일한 인스턴스인지 확인 ===
config1 id: 4364151376
config2 id: 4364151376
config1 is config2 -> True

=== 2. 상태가 공유되는지 확인 ===
[변경 전] config2.counter = 0, config2.theme = light
config1로 counter를 2번 증가시키고 theme을 'dark'로 변경
[변경 후] config2.counter = 2, config2.theme = dark

=== 3. 생성자 직접 호출 제한 확인 ===
AppConfig() 호출 -> TypeError: AppConfig는 직접 생성할 수 없습니다. AppConfig.get_instance()를 사용하세요.
```

> `id` 값은 실행할 때마다 달라질 수 있지만, 한 번의 실행 안에서 두 값은 항상 같습니다.

## 6. 설명

인스턴스는 `AppConfig` 클래스의 클래스 변수 `_instance`에 보관됩니다.
`get_instance()`는 `_instance`가 `None`인 첫 요청에서만 객체를 생성해 저장하고, 그 뒤의 요청에서는 새로 만들지 않고 저장해 둔 객체를 그대로 돌려주기 때문에 반복 요청해도 새 객체가 생기지 않습니다.
또한 `__new__`에서 예외를 던지도록 해 `AppConfig()`로 직접 만드는 경로 자체를 막았습니다.
두 변수가 하나의 인스턴스를 공유한다는 근거는, 값이 아니라 객체의 정체성을 비교하는 `is` 연산 결과가 `True`이고 `id()` 값도 동일하다는 점입니다.
실제로 `config1`으로 바꾼 `counter`와 `theme` 값이 `config2`로 읽었을 때 그대로 보이므로, 두 변수는 같은 객체를 가리키고 있습니다.
