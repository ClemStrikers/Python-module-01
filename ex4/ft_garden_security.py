class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height: float = 0.0
        else:
            self._height = height
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age: int = 0
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value

    def show(self) -> None:
        h_round: float = round(self._height, 1)
        print(f"{self._name}: {h_round}cm, {self._age} days old")


def run_security_check() -> None:
    print("=== Garden Security System ===")

    rose: Plant = Plant("Rose", 15.0, 10)
    print(f"Plant created: {rose.get_height()}cm, {rose.get_age()} days old")
    rose.set_height(25.0)
    print(f"\nHeight updated: {round(rose.get_height())}cm")
    rose.set_age(30)
    print(f"Age updated: {rose.get_age()} days\n")
    rose.set_height(-5.0)
    rose.set_age(-1)
    print("\nCurrent state: ", end="")
    rose.show()


if __name__ == "__main__":
    run_security_check()
