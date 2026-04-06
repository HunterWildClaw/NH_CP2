import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker

# Initialize Faker for procedural content
fake = Faker()

# --- 1. CORE DATA MODELS ---
# Define the Race class to represent different races with stat modifiers
class Race:
    def __init__(self, name, strength_mod, intelligence_mod, wisdom_mod, charisma_mod, dexterity_mod, constitution_mod):
        # Set the race name
        self.name = name
        # Create a dictionary of stat modifiers for each attribute
        self.mods = {
            "strength": strength_mod, "intelligence": intelligence_mod, "wisdom": wisdom_mod,
            "charisma": charisma_mod, "dexterity": dexterity_mod, "constitution": constitution_mod
        }

# Define the Class class to represent different classes with stat modifiers
class Class:
    def __init__(self, name, strength_mod, intelligence_mod, wisdom_mod, charisma_mod, dexterity_mod, constitution_mod):
        # Set the class name
        self.name = name
        # Create a dictionary of stat modifiers for each attribute
        self.mods = {
            "strength": strength_mod, "intelligence": intelligence_mod, "wisdom": wisdom_mod,
            "charisma": charisma_mod, "dexterity": dexterity_mod, "constitution": constitution_mod
        }

# Define the Character class to represent individual characters
class Character:
    def __init__(self, name, race, cls, skill, stats, backstory=None, location=None):
        # Set the character's name
        self.name = name
        # Assign the race object
        self.race = race
        # Assign the class object
        self.cls = cls
        # Assign the skill
        self.skill = skill
        # Set the stats dictionary
        self.stats = stats  # dict: {stat_name: value}
        # Generate or set backstory using Faker if not provided
        self.backstory = backstory or fake.paragraph(nb_sentences=3)
        # Generate or set location using Faker if not provided
        self.location = location or fake.city()
        # Initialize inventory as empty list
        self.inventory = []
        # Initialize inventory weight to 0
        self.inv_weight = 0
        # Set weight limit to 50
        self.weight_limit = 50

    def add_item(self, item_name, item_weight):
        # Check if adding the item would exceed the weight limit
        if self.inv_weight + item_weight > self.weight_limit:
            # Print error message and return False
            print(f"🚫 {item_name} is too heavy for {self.name}! 🚫")
            return False
        # Add the item to inventory
        self.inventory.append({"name": item_name, "weight": item_weight})
        # Update total inventory weight
        self.inv_weight += item_weight
        # Return True indicating success
        return True

    def to_dict(self):
        # Convert character data to a flat dictionary for Pandas compatibility
        # Return a dictionary with all character attributes
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
# Define DataVisualization class for plotting character stats
class DataVisualization:
    @staticmethod
    def plot_radar(char):
        # Creates a radar chart for a single character's attributes
        # Get labels from stat keys
        labels = list(char.stats.keys())
        # Get stats values
        stats = list(char.stats.values())
        
        # Calculate angles for radar chart
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
        # Close the loop for stats and angles
        stats += stats[:1]
        angles += angles[:1]

        # Create polar plot
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        # Fill the area
        ax.fill(angles, stats, color='red', alpha=0.25)
        # Plot the line
        ax.plot(angles, stats, color='red', linewidth=2)
        # Set ticks and labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([l.capitalize() for l in labels])
        # Set title
        plt.title(f"Attribute Profile: {char.name}")
        # Save the plot
        plt.savefig(f"{char.name}_radar.png")

    @staticmethod
    def plot_roster_distribution(df):
        # Visualizes the distribution of attributes across the entire roster
        # Plot box plot for selected columns
        df[["strength", "intelligence", "wisdom", "charisma", "dexterity", "constitution"]].plot(kind='box', figsize=(10,6))
        # Set title
        plt.title("Attribute Distributions Across Roster")
        # Set y-label
        plt.ylabel("Stat Value")
        # Save the plot
        plt.savefig("roster_distribution.png")

# Define StatisticalAnalyzer class for generating reports
class StatisticalAnalyzer:
    @staticmethod
    def generate_report(characters):
        # If no characters, print message and return
        if not characters:
            print("No data to analyze.")
            return
        # Create DataFrame from character dictionaries
        df = pd.DataFrame([c.to_dict() for c in characters.values()])
        # Print summary statistics
        print("\n--- ROSTER STATISTICAL SUMMARY ---")
        print(df.describe())
        # Print average stats by class
        print("\n--- AVERAGE STATS BY CLASS ---")
        numeric_cols = ["strength", "intelligence", "wisdom", "charisma", "dexterity", "constitution"]
        print(df.groupby('class')[numeric_cols].mean())

# Define RandomGenerator class for generating quests
class RandomGenerator:
    @staticmethod
    def create_quest():
        # Generates a random procedural quest
        # Return a formatted quest string using Faker
        return f"QUEST: {fake.job()} {fake.name()} needs you to travel to {fake.city()} to retrieve a {fake.color_name()} artifact."

# --- 3. MAIN CHARACTER MANAGER ---
# Define CharacterManager class to manage characters and interactions
class CharacterManager:
    def __init__(self):
        # Initialize empty dictionary for characters
        self.characters = {}
        # Define list of Race objects
        self.races = [
            Race("Elf", 1, 3, 2, 2, 2, 0),
            Race("Dwarf", 3, -1, 2, -1, 0, 1),
            Race("Orc", 3, -2, 1, -2, 2, 1),
            Race("Human", 1, 1, 1, 1, 1, 1)
        ]
        # Define list of Class objects
        self.classes = [
            Class("Mage", -1, 4, 2, 1, 0, 0),
            Class("Warrior", 4, 1, 2, 1, 2, 3),
            Class("Paladin", 2, 1, 2, 2, 1, 2)
        ]
        # Define list of skills
        self.skills = ["Archery", "Magic", "Stealth", "Swordsmanship", "Healing"]

    def attribute_roller(self):
        # Roll 6 sets of 3d6 for attributes
        rolls = [random.randint(1,6) + random.randint(1,6) + random.randint(1,6) for _ in range(6)]
        # Print the rolls
        print(f"Your rolls are: {rolls}")
        # Initialize stats dictionary
        stats = {}
        # Define stat keys
        keys = ["strength", "intelligence", "wisdom", "charisma", "dexterity", "constitution"]
        # For each stat key
        for key in keys:
            # Loop until valid assignment
            while True:
                # Try to get user input
                try:
                    val = int(input(f"Assign to {key}: "))
                    # If value is in rolls, assign and remove from rolls
                    if val in rolls:
                        stats[key] = val
                        rolls.remove(val)
                        break
                    # Else, print error
                    else: print("Roll not available.")
                # Handle invalid input
                except ValueError: print("Enter a valid number.")
        # Return the stats dictionary
        return stats

    def create_character(self):
        # Get character name from user
        name = input("Character Name: ").strip().title()
        # Display race options
        print("Select Race (1-4):")
        for i, r in enumerate(self.races, 1): print(f"{i}. {r.name}")
        # Get race choice
        race = self.races[int(input())-1]
        
        # Display class options
        print("Select Class (1-3):")
        for i, c in enumerate(self.classes, 1): print(f"{i}. {c.name}")
        # Get class choice
        cls = self.classes[int(input())-1]
        
        # Roll base stats
        base_stats = self.attribute_roller()
        # Calculate final stats with modifiers
        final_stats = {s: base_stats[s] + race.mods[s] + cls.mods[s] for s in base_stats}
        
        # Create Character object
        char = Character(name, race, cls, random.choice(self.skills), final_stats)
        # Add to characters dictionary
        self.characters[name] = char
        # Print success message
        print(f"✅ {name} created! Bio: {char.backstory[:60]}...")

    def bulk_generate(self, count):
        # For each count
        for _ in range(count):
            # Randomly select race
            race = random.choice(self.races)
            # Randomly select class
            cls = random.choice(self.classes)
            # Generate random stats with modifiers
            stats = {s: random.randint(3,18) + race.mods[s] + cls.mods[s] for s in race.mods}
            # Create Character object
            char = Character(fake.name(), race, cls, random.choice(self.skills), stats)
            # Add to characters dictionary
            self.characters[char.name] = char
            # Print generation message
            print(f"Generated: {char.name}")
        # Print total generated
        print(f"🎲 Generated {count} procedural characters.")

    def export_data(self):
        # Create DataFrame from characters
        df = pd.DataFrame([c.to_dict() for c in self.characters.values()])
        # Export to CSV
        df.to_csv("character_portfolio.csv", index=False)
        # Print success message
        print("💾 Exported to character_portfolio.csv")

    def main_menu(self):
        # Loop indefinitely for menu
        while True:
            # Print menu options
            print("\n--- RPG MANAGER ---")
            print("1. Create Character\n2. Bulk Generate NPCs (Faker)\n3. Statistical Report (Pandas)\n4. Visualize Stats (Matplotlib)\n5. Generate Random Quest\n6. Export to CSV\n7. Quit")
            # Get user choice
            choice = input("Select an option: ")
            # If choice is 1, create character
            if choice == '1': self.create_character()
            # If choice is 2, bulk generate
            elif choice == '2': self.bulk_generate(int(input("How many characters? ")))
            # If choice is 3, generate report
            elif choice == '3': StatisticalAnalyzer.generate_report(self.characters)
            # If choice is 4, visualize stats
            elif choice == '4':
                name = input("Enter character name to visualize: ")
                if name in self.characters: DataVisualization.plot_radar(self.characters[name])
                else: print("Character not found.")
            # If choice is 5, generate quest
            elif choice == '5': print(RandomGenerator.create_quest())
            # If choice is 6, export data
            elif choice == '6': self.export_data()
            # If choice is 7, break loop
            elif choice == '7': break

# If this script is run directly
if __name__ == "__main__":
    # Create CharacterManager instance
    manager = CharacterManager()
    # Start main menu
    manager.main_menu()