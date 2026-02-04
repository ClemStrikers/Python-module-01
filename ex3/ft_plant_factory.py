class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

def ft_plant_factory():
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]

    created_plants = []

    print("=== Plant Factory Output ===")

    for i in range(len(plant_data)):
        name, height, age = plant_data[i]
        
        new_plant = Plant(name, height, age)
        created_plants.append(new_plant)
        
        print(f"Created: {new_plant.name} ({new_plant.height}cm, {new_plant.age} days)")

    print(f"Total plants created: {len(created_plants)}")

if __name__ == "__main__":
    ft_plant_factory()