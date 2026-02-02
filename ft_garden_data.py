class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

def main():
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    garden = [rose, sunflower, cactus]

    print("=== Garden Plant Registry ===")

    for i in range(len(garden)):
        plant = garden[i]
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")

if __name__ == "__main__":
    main()