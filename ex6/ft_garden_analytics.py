from typing import Any


class Plant:

    class _InternalSystem:

        def __init__(self) -> None:
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, {self.show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height
        self._age_days: int = age
        self._stats: Plant._InternalSystem = self._InternalSystem()

    @staticmethod
    def is_older_than_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        self._height += 8.0
        self._stats.grow_calls += 1

    def age(self) -> None:
        self._age_days += 1
        self._stats.age_calls += 1

    def show(self) -> None:
        self._stats.show_calls += 1
        h_round: float = round(self._height, 1)
        print(f"{self._name}: {h_round}cm, {self._age_days} days old")


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed_count: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed_count}")


class Tree(Plant):

    def __init__(self, name: str, height: float, age: int, diam: float)\
          -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = diam
        self._shade_calls: int = 0

    def produce_shade(self) -> None:
        self._shade_calls += 1
        h_val: float = round(self._height, 1)
        d_val: float = round(self._trunk_diameter, 1)
        print(f"Tree {self._name} now produces a shade of "
              f"{h_val}cm long and {d_val}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")


def display_plant_stats(plant: Any) -> None:

    if hasattr(plant, "_name"):
        print(f"[statistics for {plant._name}]")

    if hasattr(plant, "_stats"):
        plant._stats.display()

    if isinstance(plant, Tree):
        print(f"{plant._shade_calls} shade")


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year?-> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year?-> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("\n=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("\n=== Seed")
    sun: Seed = Seed("Sunflower", 80.0, 45, "yellow")
    sun.show()
    print("[make sunflower grow, age and bloom]")
    sun._height += 22.0
    sun.grow()
    for _ in range(20):
        sun.age()
    sun.bloom()
    sun.show()
    display_plant_stats(sun)

    print("\n=== Anonymous")
    anon: Plant = Plant.create_anonymous()
    anon.show()
    display_plant_stats(anon)


if __name__ == "__main__":
    main()
