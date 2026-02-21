class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, amount=1):
        self.height += amount
        print(f"{self.name} grew {amount}cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, color):
        super().__init__(name, height)
        self.color = color

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

    def get_info(self):
        return f"{super().get_info()}, Prize points: {self.points}"


class GardenManager:

    _total_gardens = 0

    class GardenStats:
        @staticmethod
        def calculate_score(plants):
            """Calcule un score basé sur la taille et les points de prix."""
            score = 0
            for p in plants:
                score += p.height
                if isinstance(p, PrizeFlower):
                    score += p.points
            return score

        @staticmethod
        def count_types(plants):
            """Compte les types de plantes dans la collection."""
            reg, flow, prize = 0, 0, 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flow += 1
                else:
                    reg += 1
            return reg, flow, prize

    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.plants = []
        GardenManager._total_gardens += 1

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def help_all_grow(self, amount=1):
        print(f"{self.owner_name} is helping all plants grow...")
        for p in self.plants:
            p.grow(amount)

    @classmethod
    def create_garden_network(cls):
        """Méthode de classe agissant sur le type Manager lui-même."""
        return cls._total_gardens

    @staticmethod
    def validate_height(h):
        """Fonction utilitaire indépendante des données d'instance."""
        return h > 0

    def generate_report(self):
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for p in self.plants:
            if hasattr(p, 'get_info'):
                print(f"- {p.get_info()}")
            else:
                print(f"- {p.name}: {p.height}cm")

        reg, flow, prize = self.GardenStats.count_types(self.plants)
        print(f"Plants added: {len(self.plants)},"
              f"Total growth: {len(self.plants)}cm")
        print(f"Plant types: {reg} regular,"
              f"{flow} flowering, {prize} prize flowers")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")
    alice_garden.add_plant(Plant("Oak Tree", 100))
    alice_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    alice_garden.help_all_grow(1)
    alice_garden.generate_report()
    is_valid = GardenManager.validate_height(10)
    print(f"\nHeight validation test: {is_valid}")

    alice_score =\
        GardenManager.GardenStats.calculate_score(alice_garden.plants)
    bob_score = 92
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    print(f"Total gardens managed: {GardenManager.create_garden_network()}")
