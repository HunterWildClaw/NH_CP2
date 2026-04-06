import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker

# Initialize Faker for procedural content
fake = Faker()

# --- 1. CORE DATA MODELS ---
class Race:
    def __init__(self, name, strength_mod, intelligence_mod, wisdom_mod, charisma_mod, dexterity_mod, constitution_mod):
        self.name = name
        self.mods = {
            "strength": strength_mod, "intelligence": intelligence_mod, "wisdom": wisdom_mod,
            "charisma": charisma_mod, "dexterity": dexterity_mod, "constitution": constitution_mod
        }

class Class:
    def __init__(self, name, strength_mod, intelligence_mod, wisdom_mod, charisma_mod, dexterity_mod, constitution_mod):
        self.name = name
        self.mods = {
            "strength": strength_mod, "intelligence": intelligence_mod, "wisdom": wisdom_mod,
            "charisma": charisma_mod, "dexterity": dexterity_mod, "constitution": constitution_mod
        }

class Character:
    def __init__(self, name, race, cls, skill, stats, backstory=None, location=None):
        self.name = name
        self.race = race
        self.cls = cls
        self.skill = skill
        self.stats = stats  # dict: {stat_name: value}
        self.backstory = backstory or fake.paragraph(nb_sentences=3)
        self.location = location or fake.city()
        self.inventory = []
        self.inv_weight = 0
        self.weight_limit = 50

    def add_item(self, item_name, item_weight):
        if self.inv_weight + item_weight > self.weight_limit:
            print(f"🚫 {item_name} is too heavy for {self.name}! 🚫")
            return False
        self.inventory.append({"name": item_name, "weight": item_weight})
        self.inv_weight += item_weight
        return True

    def to_dict(self):
        """Converts character data to a flat dictionary for Pandas compatibility."""
        return {
            "name": self.name,
            "race": self.race.name,
            "class": self.cls.name,
            "skill": self.skill,
            "location": self.location,
            "backstory": self.backstory,
            **self.stats
        }

# --- 2. ENHANCED SERVICE CLASSES ---
class DataVisualization:
    @staticmethod
    def plot_radar(char):
        """Creates a radar chart for a single character's attributes."""
        labels = list(char.stats.keys())
        stats = list(char.stats.values())
        
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
        stats += stats[:1]
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.fill(angles, stats, color='red', alpha=0.25)
        ax.plot(angles, stats, color='red', linewidth=2)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([l.capitalize() for l in labels])
        plt.title(f"Attribute Profile: {char.name}")
        plt.show()

    @staticmethod
    def plot_roster_distribution(df):
        """Visualizes the distribution of attributes across the entire roster."""
        df[["strength", "intelligence", "wisdom", "charisma", "dexterity", "constitution"]].plot(kind='box', figsize=(10,6))
        plt.title("Attribute Distributions Across Roster")
        plt.ylabel("Stat Value")
        plt.show()

class StatisticalAnalyzer:
    @staticmethod
    def generate_report(characters):
        if not characters:
            print("No data to analyze.")
            return
        df = pd.DataFrame([c.to_dict() for c in characters.values()])
        print("\n--- ROSTER STATISTICAL SUMMARY ---")
        print(df.describe())
        print("\n--- AVERAGE STATS BY CLASS ---")
        numeric_cols = ["strength", "intelligence", "wisdom", "charisma", "dexterity", "constitution"]
        print(df.groupby('class')[numeric_cols].mean())

class RandomGenerator:
    @staticmethod
    def create_quest():
        """Generates a random procedural quest."""
        return f"QUEST: {fake.job()} {fake.name()} needs you to travel to {fake.city()} to retrieve a {fake.color_name()} artifact."

# --- 3. MAIN CHARACTER MANAGER ---
class CharacterManager:
    def __init__(self):
        self.characters = {}
        self.races = [
            Race("Elf", 1, 3, 2, 2, 2, 0),
            Race("Dwarf", 3, -1, 2, -1, 0, 1),
            Race("Orc", 3, -2, 1, -2, 2, 1),
            Race("Human", 1, 1, 1, 1, 1, 1)
        ]
        self.classes = [
            Class("Mage", -1, 4, 2, 1, 0, 0),
            Class("Warrior", 4, 1, 2, 1, 2, 3),
            Class("Paladin", 2, 1, 2, 2, 1, 2)
        ]
        self.skills = ["Archery", "Magic", "Stealth", "Swordsmanship", "Healing"]

    def attribute_roller(self):
        rolls = [random.randint(1,6) + random.randint(1,6) + random.randint(1,6) for _ in range(6)]
        print(f"Your rolls are: {rolls}")
        stats = {}
        keys = ["strength", "intelligence", "wisdom", "charisma", "dexterity", "constitution"]
        for key in keys:
            while True:
                try:
                    val = int(input(f"Assign to {key}: "))
                    if val in rolls:
                        stats[key] = val
                        rolls.remove(val)
                        break
                    else: print("Roll not available.")
                except ValueError: print("Enter a valid number.")
        return stats

    def create_character(self):
        name = input("Character Name: ").strip().title()
        print("Select Race (1-4):")
        for i, r in enumerate(self.races, 1): print(f"{i}. {r.name}")
        race = self.races[int(input())-1]
        
        print("Select Class (1-3):")
        for i, c in enumerate(self.classes, 1): print(f"{i}. {c.name}")
        cls = self.classes[int(input())-1]
        
        base_stats = self.attribute_roller()
        final_stats = {s: base_stats[s] + race.mods[s] + cls.mods[s] for s in base_stats}
        
        char = Character(name, race, cls, random.choice(self.skills), final_stats)
        self.characters[name] = char
        print(f"✅ {name} created! Bio: {char.backstory[:60]}...")

    def bulk_generate(self, count):
        for _ in range(count):
            race = random.choice(self.races)
            cls = random.choice(self.classes)
            stats = {s: random.randint(3,18) + race.mods[s] + cls.mods[s] for s in race.mods}
            char = Character(fake.name(), race, cls, random.choice(self.skills), stats)
            self.characters[char.name] = char
        print(f"🎲 Generated {count} procedural characters.")

    def export_data(self):
        df = pd.DataFrame([c.to_dict() for c in self.characters.values()])
        df.to_csv("character_portfolio.csv", index=False)
        print("💾 Exported to character_portfolio.csv")

    def main_menu(self):
        while True:
            print("\n--- RPG MANAGER ---")
            print("1. Create Character\n2. Bulk Generate NPCs (Faker)\n3. Statistical Report (Pandas)\n4. Visualize Stats (Matplotlib)\n5. Generate Random Quest\n6. Export to CSV\n7. Quit")
            choice = input("Select an option: ")
            if choice == '1': self.create_character()
            elif choice == '2': self.bulk_generate(int(input("How many characters? ")))
            elif choice == '3': StatisticalAnalyzer.generate_report(self.characters)
            elif choice == '4':
                name = input("Enter character name to visualize: ")
                if name in self.characters: DataVisualization.plot_radar(self.characters[name])
                else: print("Character not found.")
            elif choice == '5': print(RandomGenerator.create_quest())
            elif choice == '6': self.export_data()
            elif choice == '7': break

if __name__ == "__main__":
    manager = CharacterManager()
    manager.main_menu()