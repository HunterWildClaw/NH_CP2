from dataclasses import dataclass
from enum import Enum
from typing import List

class Race(Enum):
    HUMAN = "Human"
    ORC = "Orc"
    DWARF = "Dwarf"
    NIGHT_ELF = "Night Elf"
    TAUREN = "Tauren"
    GNOME = "Gnome"
    TROLL = "Troll"
    BLOOD_ELF = "Blood Elf"
    DRAENEI = "Draenei"
    GOBLIN = "Goblin"
    WORGEN = "Worgen"
    PANDAREN = "Pandaren"

class Class(Enum):
    WARRIOR = "Warrior"
    PALADIN = "Paladin"
    HUNTER = "Hunter"
    ROGUE = "Rogue"
    PRIEST = "Priest"
    DEATH_KNIGHT = "Death Knight"
    SHAMAN = "Shaman"
    MAGE = "Mage"
    WARLOCK = "Warlock"
    MONK = "Monk"
    DRUID = "Druid"

@dataclass
class Character:
    name: str
    race: Race
    char_class: Class
    level: int = 1
    experience: int = 0
    health: int = 100
    mana: int = 100
    
    def __str__(self):
        return f"{self.name} - {self.race.value} {self.char_class.value} (Level {self.level})"
    
    def gain_experience(self, amount: int):
        self.experience += amount
        if self.experience >= 1000:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.experience = 0
        self.health += 10
        self.mana += 10

class CharacterCreator:
    def __init__(self):
        self.characters: List[Character] = []
    
    def create_character(self, name: str, race: Race, char_class: Class) -> Character:
        char = Character(name, race, char_class)
        self.characters.append(char)
        return char
    
    def list_characters(self) -> List[Character]:
        return self.characters
    
    def delete_character(self, name: str) -> bool:
        for char in self.characters:
            if char.name == name:
                self.characters.remove(char)
                return True
        return False

def display_options(options: dict):
    for key, value in options.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    creator = CharacterCreator()
    
    while True:
        print("\n=== Character Creator ===")
        print("1. Create Character")
        print("2. List Characters")
        print("3. Delete Character")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            name = input("Enter character name: ").strip()
            
            print("Select Race:")
            races = {str(i+1): race for i, race in enumerate(Race)}
            display_options(races)
            race_choice = input("Choose race (number): ").strip()
            race = races.get(race_choice, Race.HUMAN)
            
            print("Select Class:")
            classes = {str(i+1): cls for i, cls in enumerate(Class)}
            display_options(classes)
            class_choice = input("Choose class (number): ").strip()
            char_class = classes.get(class_choice, Class.WARRIOR)
            
            char = creator.create_character(name, race, char_class)
            print(f"✓ Created: {char}")
        
        elif choice == "2":
            chars = creator.list_characters()
            if chars:
                print("\nCharacters:")
                for char in chars:
                    print(f"  {char}")
            else:
                print("No characters created yet.")
        
        elif choice == "3":
            name = input("Enter character name to delete: ").strip()
            if creator.delete_character(name):
                print(f"✓ Deleted {name}")
            else:
                print(f"✗ Character '{name}' not found")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")