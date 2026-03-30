from typing import List


class Plant:

    def __init__(self, name: str, height: float, age_days: int) -> None:

        self.name: str = name
        self.height: float = height
        self.age_days: int = age_days

    def grow(self, amount: float = 0.5) -> None:
        self.height += amount

    def show(self) -> None:
        h_round: float = round(self.height, 1)
        print(f"Created: {self.name}: {h_round}cm, {self.age_days} days old")


def start_factory() -> None:
    print("=== Plant Factory Output ===")

    garden: List[Plant] = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]

    for i in range(len(garden)):
        garden[i].show()


if __name__ == "__main__":
    start_factory()
