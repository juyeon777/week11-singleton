"""Singleton 동작 확인용 실행 코드."""

from singleton import AppConfig


def main():
    print("=== 1. 동일한 인스턴스인지 확인 ===")
    config1 = AppConfig.get_instance()
    config2 = AppConfig.get_instance()
    print(f"config1 id: {id(config1)}")
    print(f"config2 id: {id(config2)}")
    print(f"config1 is config2 -> {config1 is config2}")

    print()
    print("=== 2. 상태가 공유되는지 확인 ===")
    print(f"[변경 전] config2.counter = {config2.counter}, config2.theme = {config2.theme}")
    config1.increment()
    config1.increment()
    config1.theme = "dark"
    print("config1로 counter를 2번 증가시키고 theme을 'dark'로 변경")
    print(f"[변경 후] config2.counter = {config2.counter}, config2.theme = {config2.theme}")

    print()
    print("=== 3. 생성자 직접 호출 제한 확인 ===")
    try:
        AppConfig()
    except TypeError as e:
        print(f"AppConfig() 호출 -> TypeError: {e}")


if __name__ == "__main__":
    main()
