class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = self.trunk_diameter * 1.56
        print(f"{self.name} provides {int(shade_area)} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,  har_season, n_value):
        super().__init__(name, height, age)
        self.harvest_season = har_season
        self.nutritional_value = n_value


def main():
    print("=== Garden Plant Types ===")

    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 80, 45, "yellow")
    print(f"\n{rose.name} (Flower): "
          f"{rose.height}cm, "
          f"{rose.age} days, "
          f"{rose.color} color")
    rose.bloom()
    print(f"\n{sunflower.name} (Flower): {sunflower.height}cm, "
          f"{sunflower.age} days, {sunflower.color} color")
    sunflower.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    cherry_tree = Tree("Cherry tree", 200, 730, 35)
    print(f"\n{oak.name} (Tree): {oak.height}cm, {oak.age} days, "
          f"{oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    print(f"\n{cherry_tree.name} (Tree): {cherry_tree.height}cm,"
          f" {cherry_tree.age} days, "
          f"{cherry_tree.trunk_diameter}cm diameter")
    cherry_tree.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 20, 60, "autumn", "beta-carotene")
    print(f"\n{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days,"
          f"{tomato.harvest_season} harvest")
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
    print(f"\n{carrot.name} (Vegetable): {carrot.height}cm, {carrot.age} days,"
          f"{carrot.harvest_season} harvest")
    print(f"{carrot.name} is rich in {carrot.nutritional_value}")


if __name__ == "__main__":
    main()
