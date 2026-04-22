class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, {self._age_calls} age, "
                  f"{self._show_calls} show")

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_days: int = age
        self.stats = self.Stats()

    @staticmethod
    def is_older_than_a_year(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self) -> None:
        self.height += 1.0
        self.stats.record_grow()

    def age(self) -> None:
        self.age_days += 1
        self.stats.record_age()

    def show(self) -> None:
        self.stats.record_show()
        h_round: float = round(self.height, 1)
        print(f"{self.name}: {h_round}cm, {self.age_days} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    class TreeStats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.tree_stats = self.TreeStats()
        self.stats = self.tree_stats
        self.trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        self.tree_stats.record_shade()
        h_val: float = round(self.height, 1)
        d_val: float = round(self.trunk_diameter, 1)
        print(f"Tree {self.name} now produces a shade of "
              f"{h_val}cm long and {d_val}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutritional_value: int = 0

    def grow(self) -> None:
        self.height += 2.1
        self.nutritional_value += 1
        self.stats.record_grow()

    def age(self) -> None:
        super().age()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds: int = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year?-> "
          f"{Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year?-> "
          f"{Plant.is_older_than_a_year(400)}")

    print("Object-Oriented Garden Systems")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.height += 7.0
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.height += 29.0
    sunflower.grow()
    sunflower.age_days += 19
    sunflower.age()
    sunflower.seeds = 42
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_statistics(anon)


if __name__ == "__main__":
    main()
