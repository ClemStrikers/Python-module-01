class Plant:

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days
        self.growth_rate: float = 0.5

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.age_days += 1

    def show(self) -> None:
        current_height: float = round(self.height, 1)
        print(f"{self.name}: {current_height}cm, {self.age_days} days old")


class Rose(Plant):

    def __init__(self, name: str, height: float, age_days: int) -> None:

        super().__init__(name, height, age_days)
        self.growth_rate = 0.8


def run_simulation() -> None:
    rose: Rose = Rose("Rose", 25.0, 30)
    initial_height: float = rose.height

    print("=== Garden Plant Growth ===")

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.show()
        rose.grow()
        rose.age()
    total_increase: float = rose.height - initial_height
    print(f"Growth this week: {round(total_increase)}cm")


if __name__ == "__main__":
    run_simulation()
