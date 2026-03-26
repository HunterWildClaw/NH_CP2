#NH 2nd Video Game character creator
#Import Random, OS, and CSV
import random
import csv
import os

class Character:
    #Represents a video game character with stats and abilities.
    
    # Class stat templates
    classes = {
        "Warrior": {"health": 120, "attack": 15, "defense": 20},
        "Mage": {"health": 75, "attack": 25, "defense": 10},
        "Archer": {"health": 100, "attack": 20, "defense": 15}
    }
    
    def __init__(self, name, character_class):
        #Initialize a character with name and class.
        self.name = name
        self.character_class = character_class
        self.level = 1
        stats = self.classes[character_class]
        self.max_health = stats["health"]
        self.health = stats["health"]
        self.attack = stats["attack"]
        self.defense = stats["defense"]
    
    def display_info(self):
        #Display character information.
        print(f"\n   Name: {self.name}")
        print(f"   Class: {self.character_class}")
        print(f"   Level: {self.level}")
        print(f"   Health: {self.health}/{self.max_health}")
        print(f"   Attack: {self.attack}")
        print(f"   Defense: {self.defense}")
    
    def level_up(self):
        #Increase character level and stats.
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        self.attack += 5
        self.defense += 3
        print(f"\n✅ {self.name} leveled up to Level {self.level}!")
        self.display_info()
    
    def take_damage(self, damage):
        #Reduce health by damage amount.
        actual_damage = max(1, damage - self.defense // 2)
        self.health -= actual_damage
        self.health = max(0, self.health)
        return actual_damage
    
    def restore_health(self):
        #Restore character to full health.
        self.health = self.max_health
    
    def is_alive(self):
        #Check if character is still alive.
        return self.health > 0


class Game:
    #Manages a collection of characters and game operations.
    
    CSV_FILE = "characters.csv"
    
    def __init__(self):
        #Initialize game with empty character list.#
        self.characters = []
        self.load_characters()
    
    def add_character(self, character):
        #Add a character to the game.#
        if any(c.name.lower() == character.name.lower() for c in self.characters):
            print(f"❌ Character '{character.name}' already exists!")
            return False
        self.characters.append(character)
        self.save_characters()
        return True
    
    def find_character(self, name):
        #Find character by name.#
        for character in self.characters:
            if character.name.lower() == name.lower():
                return character
        return None
    
    def get_all_characters(self):
        #Return list of all characters.#
        return self.characters
    
    def save_characters(self):
        #Save all characters to CSV file.#
        try:
            with open(self.CSV_FILE, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Class", "Level", "Max Health", "Health", "Attack", "Defense"])
                for char in self.characters:
                    writer.writerow([char.name, char.character_class, char.level, char.max_health, char.health, char.attack, char.defense])
            print(f"✅ Characters saved to {self.CSV_FILE}")
        except Exception as e:
            print(f"❌ Error saving characters: {e}")
    
    def load_characters(self):
        #Load characters from CSV file.#
        if not os.path.exists(self.CSV_FILE):
            return
        
        try:
            with open(self.CSV_FILE, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    char = Character(row["Name"], row["Class"])
                    char.level = int(row["Level"])
                    char.max_health = int(row["Max Health"])
                    char.health = int(row["Health"])
                    char.attack = int(row["Attack"])
                    char.defense = int(row["Defense"])
                    self.characters.append(char)
            print(f"✅ Loaded {len(self.characters)} character(s) from {self.CSV_FILE}")
        except Exception as e:
            print(f"❌ Error loading characters: {e}")
    
    def battle(self, char1_name, char2_name):
        #Simulate a battle between two characters.#
        char1 = self.find_character(char1_name)
        char2 = self.find_character(char2_name)
        
        if not char1 or not char2:
            print("❌ One or both characters not found!")
            return
        
        if char1_name.lower() == char2_name.lower():
            print("❌ A character cannot battle themselves!")
            return
        
        # Restore health for battle
        char1.restore_health()
        char2.restore_health()
        
        print(f"\n🥊 BATTLE BEGINS!")
        print(f"{char1.name} vs {char2.name}\n")
        
        round_num = 1
        while char1.is_alive() and char2.is_alive():
            print(f"--- Round {round_num} ---")
            
            # Char1 attacks
            damage = random.randint(char1.attack - 5, char1.attack + 5)
            actual_damage = char2.take_damage(damage)
            print(f"{char1.name} attacks {char2.name} for {actual_damage} damage!")
            print(f"{char2.name}'s health: {char2.health}/{char2.max_health}\n")
            
            if not char2.is_alive():
                break
            
            # Char2 attacks
            damage = random.randint(char2.attack - 5, char2.attack + 5)
            actual_damage = char1.take_damage(damage)
            print(f"{char2.name} attacks {char1.name} for {actual_damage} damage!")
            print(f"{char1.name}'s health: {char1.health}/{char1.max_health}\n")
            
            round_num += 1
            
            if round_num > 20:  # Prevent infinite battles
                print("⚔️ Battle is a draw!")
                self.save_characters()
                return
        
        # Declare winner
        if char1.is_alive():
            print(f"🏆 {char1.name} wins!")
        else:
            print(f"🏆 {char2.name} wins!")
        
        self.save_characters()


def display_menu():
    #Display main menu and return user choice.
    print("\n" + "=" * 37)
    print("⚔️ CHARACTER CREATOR ⚔️")
    print("=" * 37)
    print("\n🎮 MAIN MENU:")
    print("[1] Create New Character")
    print("[2] View Character")
    print("[3] Level Up Character")
    print("[4] Battle Characters")
    print("[5] View All Characters")
    print("[6] Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-6): ")
            if choice in ["1", "2", "3", "4", "5", "6"]:
                return choice
            print("❌ Invalid choice! Please enter 1-6.")
        except KeyboardInterrupt:
            return "6"


def create_character(game):
    #Handle character creation.
    print("\n" + "=" * 37)
    print("✨ CREATE CHARACTER ✨")
    print("=" * 37)
    
    while True:
        name = input("\nEnter character name: ").strip()
        if name and len(name) >= 1:
            break
        print("❌ Name must be at least 2 characters long.")
    
    print("\nChoose character class:")
    print("[1] Warrior (High Health & Defense)")
    print("[2] Mage (High Attack, Low Health)")
    print("[3] Archer (Balanced Stats)")
    
    class_map = {"1": "Warrior", "2": "Mage", "3": "Archer"}
    while True:
        choice = input("\nEnter class choice (1-3): ")
        if choice in class_map:
            character_class = class_map[choice]
            break
        print("❌ Invalid choice! Please enter 1-3.")
    
    character = Character(name, character_class)
    if game.add_character(character):
        print("\n✅ Character created successfully!")
        character.display_info()
    
    input("\nPress Enter to continue...")


def view_character(game):
    #Handle viewing character details.
    if not game.get_all_characters():
        print("\n❌ No characters created yet!")
        input("Press Enter to continue...")
        return
    
    print("\n" + "=" * 37)
    print("👤 VIEW CHARACTER 👤")
    print("=" * 37)
    
    name = input("\nEnter character name: ").strip()
    character = game.find_character(name)
    
    if character:
        character.display_info()
    else:
        print(f"❌ Character '{name}' not found!")
    
    input("\nPress Enter to continue...")


def level_up_character(game):
    #Handle leveling up a character.
    if not game.get_all_characters():
        print("\n❌ No characters created yet!")
        input("Press Enter to continue...")
        return
    
    print("\n" + "=" * 37)
    print("📈 LEVEL UP CHARACTER 📈")
    print("=" * 37)
    
    name = input("\nEnter character name: ").strip()
    character = game.find_character(name)
    
    if character:
        character.level_up()
        game.save_characters()
    else:
        print(f"❌ Character '{name}' not found!")
    
    input("\nPress Enter to continue...")


def battle_characters(game):
    #Handle character battles.
    if len(game.get_all_characters()) < 2:
        print("\n❌ Need at least 2 characters to battle!")
        input("Press Enter to continue...")
        return
    
    print("\n" + "=" * 37)
    print("⚔️ BATTLE ARENA ⚔️")
    print("=" * 37)
    
    print("\nAvailable Characters:")
    for char in game.get_all_characters():
        print(f"- {char.name} ({char.character_class}, Level {char.level})")
    
    char1_name = input("\nEnter first fighter: ").strip()
    char2_name = input("Enter second fighter: ").strip()
    
    game.battle(char1_name, char2_name)
    input("\nPress Enter to continue...")


def view_all_characters(game):
    #Display all characters in a table.
    characters = game.get_all_characters()
    
    if not characters:
        print("\n❌ No characters created yet!")
        input("Press Enter to continue...")
        return
    
    print("\n" + "=" * 37)
    print("👥 ALL CHARACTERS 👥")
    print("=" * 37)
    
    print("\n┌──────────────────────────────────────┐")
    print("│ Name    │ Class   │ Lvl │ HP   │ Atk │")
    print("├──────────────────────────────────────┤")
    
    for char in characters:
        print(f"│ {char.name:<7} │ {char.character_class:<7} │ {char.level:<3} │ {char.health:<4} │ {char.attack:<3} │")
    
    print("└──────────────────────────────────────┘")
    input("\nPress Enter to continue...")


def main():
    #Main game loop.
    game = Game()
    
    print("\n" + "=" * 37)
    print("⚔️ CHARACTER CREATOR ⚔️")
    print("=" * 37)
    print("\nWelcome to the Character Creator!")
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            create_character(game)
        elif choice == "2":
            view_character(game)
        elif choice == "3":
            level_up_character(game)
        elif choice == "4":
            battle_characters(game)
        elif choice == "5":
            view_all_characters(game)
        elif choice == "6":
            print("\n👋 Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()