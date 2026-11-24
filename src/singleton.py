"""Singleton 패턴 구현 (Python)."""


class AppConfig:
    """프로그램 전체에서 단 하나만 존재하는 설정 객체."""

    # 유일한 인스턴스를 보관하는 클래스 변수
    _instance = None

    def __new__(cls, *args, **kwargs):
        # AppConfig() 처럼 생성자를 직접 호출하는 것을 막는다.
        raise TypeError(
            "AppConfig는 직접 생성할 수 없다. AppConfig.get_instance()를 사용할 것."
        )

    @classmethod
    def get_instance(cls):
        # 처음 요청할 때만 객체를 만들고, 이후에는 보관된 객체를 그대로 돌려준다.
        if cls._instance is None:
            instance = object.__new__(cls)  # 막아 둔 __new__를 우회해 내부에서만 생성
            instance.counter = 0
            instance.theme = "light"
            cls._instance = instance
        return cls._instance

    def increment(self):
        self.counter += 1
        return self.counter
