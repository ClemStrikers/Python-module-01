class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int):
        self.height += cm

    def age_one_day(self):
        self.age += 1

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def simulate_week(plants):
    print("=== Day 1 ===")
    for p in plants:
        print(p.get_info())

    initial_heights = [p.height for p in plants]

    for _ in range(6):
        for p in plants:
            p.grow(1)
            p.age_one_day()

    print("=== Day 7 ===")
    for i in range(len(plants)):
        p = plants[i]
        print(p.get_info())
        growth = p.height - initial_heights[i]
        print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    my_garden = [rose]
    simulate_week(my_garden)
