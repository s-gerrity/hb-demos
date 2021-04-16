class Animal:
    """An Animal."""

    happiness_multiplier = 1.0

    def __init__(self, name, species):
        """Create an Animal with a name and species.

        All animals start with a health and happiness of 1.0 (or 100%).
        """

        self.name = name.capitalize()
        self.species = species

        self.hunger = 0
        self.happiness = 1.0

        print("A new animal was born!")

    def pet(self):
        """Pet the animal. Animals love pats."""

        self.happiness += 0.5 * self.happiness_multiplier

    def feed(self):
        """Feed the animal. Animals love eating."""

        self.hunger -= 0.5

    @property
    def info(self):
        return f"{self.name} the {self.species}"

    @property
    def stats(self):
        return f"Hunger: {self.hunger}\nHappiness: {self.happiness}"

    def print(self):
        """Print a formatted version of an animal's stats."""

        print(self.info)
        print(f"    {self.stats}")

    @classmethod
    def print_animals(cls, animals):
        """Print statuses for a collection of animals."""

        for animal in animals:
            animal.print()
            print()


