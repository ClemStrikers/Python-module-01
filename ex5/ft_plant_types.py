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
    def __init__(self, name: str, height: int, age: int,  harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

def main():
    print("=== Garden Plant Types ===")
    
    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("Sunflower", 80, 45, "yellow")
    print(f"{rose.name} (Flower): {rose.height}cm, {rose.age} days, {rose.color} color")
    rose.bloom()
    print(f"{sunflower.name} (Flower): {sunflower.height}cm, {sunflower.age} days, {sunflower.color} color")
    sunflower.bloom()

    oak = Tree("Oak", 500, 1825, 50)
    cherry_tree = Tree("Cherry tree", 200, 730, 35)
    print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    print(f"{cherry_tree.name} (Tree): {cherry_tree.height}cm, {cherry_tree.age} days, {cherry_tree.trunk_diameter}cm diameter")
    cherry_tree.produce_shade()

    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 20, 60, "autumn", "beta-carotene")
    print(f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, {tomato.harvest_season} harvest")
    print(f"{tomato.name} is rich in {tomato.nutritional_value}")
    print(f"{carrot.name} (Vegetable): {carrot.height}cm, {carrot.age} days, {carrot.harvest_season} harvest")
    print(f"{carrot.name} is rich in {carrot.nutritional_value}")

if __name__ == "__main__":
    main()