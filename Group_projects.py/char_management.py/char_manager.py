# NH, BR 2nd character creator - Enhanced with OOP, Data Visualization, Statistical Analysis, and Random Data Generation
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Race:
    def __init__(self, name, strength_mod, intelligence_mod, wisdom_mod, charisma_mod, dexterity_mod, constitution_mod):
        self.name = name
        self.mods = {
            "strength": strength_mod,
            "intelligence": intelligence_mod,
            "wisdom": wisdom_mod,
            "charisma": charisma_mod,
            "dexterity": dexterity_mod,
            "constitution": constitution_mod
        }

class Class:
    def __init__(self, name, strength_mod, intelligence_mod, wisdom_mod, charisma_mod, dexterity_mod, constitution_mod):
        self.name = name
        self.mods = {
            "strength": strength_mod,
            "intelligence": intelligence_mod,
            "wisdom": wisdom_mod,
            "charisma": charisma_mod,
            "dexterity": dexterity_mod,
            "constitution": constitution_mod
        }

class Character:
    def __init__(self, name, race, cls, skill, stats):
        self.name = name
        self.race = race
        self.cls = cls
        self.skill = skill
        self.stats = stats  # dict: strength, intelligence, etc.
        self.inventory = []  # list of dicts: {"name": str, "weight": int}
        self.inv_weight = 0
        self.weight_limit = 50

    def add_item(self, item_name, item_weight):
        if self.inv_weight + item_weight > self.weight_limit:
            print("🚫Item too heavy for remaining capacity.🚫")
            return False
        self.inventory.append({"name": item_name, "weight": item_weight})
        self.inv_weight += item_weight
        print(f"Added {item_name}!")
        return True

    def equip_item(self, index):
        if 0 <= index < len(self.inventory):
            print(f"Equipped {self.inventory[index]['name']}!")
        else:
            print("Invalid selection.")

    def delete_item(self, index):
        if 0 <= index < len(self.inventory):
            removed = self.inventory.pop(index)
            self.inv_weight -= removed['weight']
            print(f"Deleted {removed['name']}!")
        else:
            print("Invalid selection.")

    def view_inventory(self):
        if not self.inventory:
            print("💨Inventory is empty!💨")
        else:
            print("\n💰Your Inventory💰")
            for i, item in enumerate(self.inventory, 1):
                print(f"{i}. {item['name']} (Weight: {item['weight']})")
            print(f"Total weight: {self.inv_weight}/{self.weight_limit}\n")

class CharacterManager:
    def __init__(self):
        self.characters = {}
        self.races = [
            Race("Elves", 1, 3, 2, 2, 2, 0),
            Race("Dwarves", 3, -1, 2, -1, 0, 1),
            Race("Orcs", 3, -2, 1, -2, 2, 1),
            Race("Goblins", 0, 1, 1, -1, 2, 2),
            Race("Halflings", 0, 1, 0, 0, 2, 1),
        ]
        self.classes = [
            Class("Paladin", 2, 1, 2, 2, 1, 2),
            Class("Rogue", 1, 2, 1, 2, 4, 1),
            Class("Monk", 1, 2, 2, 1, 2, 1),
            Class("Mage", -1, 4, 2, 1, 0, 0),
            Class("Hunter", 2, 1, 2, 0, 2, 2),
            Class("Warrior", 4, 1, 2, 1, 2, 3),
            Class("Druid", 2, 3, 4, 1, 2, 3),
        ]
        self.skills = ["Archery", "Swordsmanship", "Magic", "Stealth", "Healing", "Intimidation"]

    def attribute_roller(self):
        attribute_rolls = [str(random.randint(1,6) + random.randint(1,6) + random.randint(1,6)) for _ in range(6)]
        print("Your attribute options are: ")
        for roll in attribute_rolls:
            print(roll)
        def checker(key):
            while True:
                attribute = input(f"Which roll do you want to choose for your {key}? ").strip()
                if attribute in attribute_rolls:
                    attribute_rolls.remove(attribute)
                    return int(attribute)
                else:
                    print("Invalid choice, try again.")
        strength = checker("strength")
        intelligence = checker("intelligence")
        wisdom = checker("wisdom")
        dexterity = checker("dexterity")
        charisma = checker("charisma")
        constitution = checker("constitution")
        return {
            "strength": strength,
            "intelligence": intelligence,
            "wisdom": wisdom,
            "charisma": charisma,
            "dexterity": dexterity,
            "constitution": constitution
        }

    def create_character(self):
        # Select race
        while True:
            print("Available races:")
            for i, race in enumerate(self.races, 1):
                print(f"{i}. {race.name}")
            try:
                race_index = int(input("What race would you like? (Enter number): ").strip()) - 1
                if 0 <= race_index < len(self.races):
                    selected_race = self.races[race_index]
                    break
                else:
                    print("🚫That input was invalid. Please try again.🚫")
            except ValueError:
                print("🚫That input was invalid. Please try again.🚫")

        # Select class
        while True:
            print("Available classes:")
            for i, cls in enumerate(self.classes, 1):
                print(f"{i}. {cls.name}")
            try:
                class_index = int(input("What class would you like? (Enter number): ").strip()) - 1
                if 0 <= class_index < len(self.classes):
                    selected_class = self.classes[class_index]
                    break
                else:
                    print("🚫That input was invalid. Please try again.🚫")
            except ValueError:
                print("🚫That input was invalid. Please try again.🚫")

        # Select name
        while True:
            character_name = input("What name do you want for your character? ").strip().title()
            if character_name in self.characters:
                print("🚫That name already exists. Please try again.🚫")
            else:
                break

        # Roll attributes
        base_stats = self.attribute_roller()

        # Apply modifiers
        final_stats = {}
        for stat in base_stats:
            final_stats[stat] = base_stats[stat] + selected_race.mods[stat] + selected_class.mods[stat]

        # Select skill
        while True:
            print("Your possible skills are: ")
            for i, skill in enumerate(self.skills, 1):
                print(f"{i}. {skill}")
            try:
                skill_index = int(input("What skill would you like? (Enter number): ").strip()) - 1
                if 0 <= skill_index < len(self.skills):
                    selected_skill = self.skills[skill_index]
                    break
                else:
                    print("That input was invalid. Please try again.")
            except ValueError:
                print("That input was invalid. Please try again.")

        # Create character
        char = Character(character_name, selected_race, selected_class, selected_skill, final_stats)
        self.characters[character_name] = char
        print(f"Character {character_name} created!")

    def search_character(self):
        while True:
            name = input("What is the name of your character? (or type 'quit' to leave): ").title().strip()
            if name == "Quit":
                break
            elif name in self.characters:
                char = self.characters[name]
                print(f"Name: {char.name}")
                print(f"Race: {char.race.name}")
                print(f"Class: {char.cls.name}")
                print(f"Skill: {char.skill}")
                print("Stats:")
                for stat, val in char.stats.items():
                    print(f"  {stat.capitalize()}: {val}")
                break
            else:
                print("That was not a name in the list of characters.")

    def manage_inventory(self, char_name):
        if char_name not in self.characters:
            print("Character not found.")
            return
        char = self.characters[char_name]
        while True:
            user_choice = input("Would you like to: \n1. Add an item \n2. Equip a pre-existent item \n3. Delete an item \n4. View inventory \n5. Leave inventory\nInsert number: ").strip()
            if user_choice == '1':
                if char.inv_weight >= char.weight_limit:
                    print("🚫You can't add anything - inventory is full!🚫")
                else:
                    item_name = input("Enter item name: ").strip().title()
                    try:
                        item_weight = int(input("Enter item weight: ").strip())
                        char.add_item(item_name, item_weight)
                    except ValueError:
                        print("🚫Invalid weight input.🚫")
            elif user_choice == '2':
                if not char.inventory:
                    print("💨Nothing in inventory to equip!💨")
                else:
                    for i, item in enumerate(char.inventory, 1):
                        print(f"{i}. {item['name']} (Weight: {item['weight']})")
                    try:
                        choice = int(input("Select item number: ").strip()) - 1
                        char.equip_item(choice)
                    except ValueError:
                        print("Invalid input.")
            elif user_choice == '3':
                if not char.inventory:
                    print("💨Nothing in inventory to delete!💨")
                else:
                    for i, item in enumerate(char.inventory, 1):
                        print(f"{i}. {item['name']}")
                    try:
                        choice = int(input("Select item to delete: ").strip()) - 1
                        char.delete_item(choice)
                    except ValueError:
                        print("Invalid input.")
            elif user_choice == '4':
                char.view_inventory()
            elif user_choice == '5':
                break
            else:
                print("🚫Invalid input. Please try again.🚫")

    def generate_random_characters(self, num):
        for _ in range(num):
            race = random.choice(self.races)
            cls = random.choice(self.classes)
            skill = random.choice(self.skills)
            name = f"RandomChar{random.randint(1000,9999)}"
            while name in self.characters:
                name = f"RandomChar{random.randint(1000,9999)}"
            base_stats = {stat: random.randint(3,18) for stat in ["strength", "intelligence", "wisdom", "charisma", "dexterity", "constitution"]}
            final_stats = {stat: base_stats[stat] + race.mods[stat] + cls.mods[stat] for stat in base_stats}
            char = Character(name, race, cls, skill, final_stats)
            self.characters[name] = char
        print(f"Generated {num} random characters.")

    def statistical_analysis(self):
        if not self.characters:
            print("No characters to analyze.")
            return
        df = pd.DataFrame([{**char.stats, "race": char.race.name, "class": char.cls.name, "skill": char.skill} for char in self.characters.values()])
        print("Statistical Summary:")
        print(df.describe())
        print("\nRace Distribution:")
        print(df['race'].value_counts())
        print("\nClass Distribution:")
        print(df['class'].value_counts())

    def visualize_data(self):
        if not self.characters:
            print("No characters to visualize.")
            return
        df = pd.DataFrame([{**char.stats, "race": char.race.name, "class": char.cls.name} for char in self.characters.values()])
        # Plot average stats by race
        race_avg = df.groupby('race').mean()
        race_avg.plot(kind='bar', figsize=(10,6))
        plt.title('Average Stats by Race')
        plt.ylabel('Average Value')
        plt.show()
        # Plot stat distributions
        df[['strength', 'intelligence', 'wisdom', 'charisma', 'dexterity', 'constitution']].hist(bins=10, figsize=(12,8))
        plt.suptitle('Stat Distributions')
        plt.show()

    def main_menu(self):
        while True:
            check = input("Do you want to: \n1. Create a character \n2. Find a character \n3. Manage inventory \n4. Generate random characters \n5. Statistical analysis \n6. Visualize data \n7. Quit \n").strip()
            if check == '1':
                self.create_character()
            elif check == '2':
                self.search_character()
            elif check == '3':
                char_name = input("Enter character name: ").strip().title()
                self.manage_inventory(char_name)
            elif check == '4':
                try:
                    num = int(input("How many random characters? ").strip())
                    self.generate_random_characters(num)
                except ValueError:
                    print("Invalid number.")
            elif check == '5':
                self.statistical_analysis()
            elif check == '6':
                self.visualize_data()
            elif check == '7':
                break
            else:
                print("🚫That was an invalid input. Please try again. 🚫")

# Run the manager
manager = CharacterManager()
manager.main_menu()