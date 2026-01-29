from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict
import random

#Buckle up!
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

# Racial bonuses
RACE_ATTRIBUTES = {
    Race.HUMAN: {"strength": 2, "dexterity": 1, "constitution": 2, "intelligence": 1, "wisdom": 1, "charisma": 2},
    Race.ORC: {"strength": 3, "dexterity": 0, "constitution": 2, "intelligence": 0, "wisdom": 1, "charisma": 0},
    Race.DWARF: {"strength": 1, "dexterity": 0, "constitution": 3, "intelligence": 1, "wisdom": 2, "charisma": 0},
    Race.NIGHT_ELF: {"strength": 0, "dexterity": 3, "constitution": 1, "intelligence": 1, "wisdom": 2, "charisma": 1},
    Race.TAUREN: {"strength": 3, "dexterity": 0, "constitution": 3, "intelligence": 0, "wisdom": 1, "charisma": 1},
    Race.GNOME: {"strength": 0, "dexterity": 2, "constitution": 1, "intelligence": 3, "wisdom": 0, "charisma": 1},
    Race.TROLL: {"strength": 2, "dexterity": 2, "constitution": 1, "intelligence": 0, "wisdom": 0, "charisma": 0},
    Race.BLOOD_ELF: {"strength": 0, "dexterity": 2, "constitution": 1, "intelligence": 2, "wisdom": 1, "charisma": 3},
    Race.DRAENEI: {"strength": 1, "dexterity": 1, "constitution": 2, "intelligence": 2, "wisdom": 2, "charisma": 1},
    Race.GOBLIN: {"strength": 1, "dexterity": 3, "constitution": 0, "intelligence": 2, "wisdom": 0, "charisma": 1},
    Race.WORGEN: {"strength": 2, "dexterity": 2, "constitution": 2, "intelligence": 1, "wisdom": 1, "charisma": 1},
    Race.PANDAREN: {"strength": 2, "dexterity": 1, "constitution": 3, "intelligence": 1, "wisdom": 2, "charisma": 2},
}

# Class skills
CLASS_SKILLS = {
    Class.WARRIOR: ["Slash", "Shield Bash", "Whirlwind Attack", "Taunt"],
    Class.PALADIN: ["Holy Strike", "Divine Shield", "Consecration", "Blessing"],
    Class.HUNTER: ["Aimed Shot", "Multi-Shot", "Pet Attack", "Disengage"],
    Class.ROGUE: ["Backstab", "Poison Strike", "Stealth", "Evasion"],
    Class.PRIEST: ["Holy Blast", "Mind Flay", "Heal", "Power Word Shield"],
    Class.DEATH_KNIGHT: ["Death Strike", "Death Coil", "Unholy Aura", "Anti-Magic Shell"],
    Class.SHAMAN: ["Lightning Bolt", "Earthquake", "Totem", "Chain Heal"],
    Class.MAGE: ["Fireball", "Frost Bolt", "Arcane Blast", "Teleport"],
    Class.WARLOCK: ["Chaos Bolt", "Drain Life", "Summon Demon", "Curse"],
    Class.MONK: ["Tiger Strike", "Crane Kick", "Chi Burst", "Meditation"],
    Class.DRUID: ["Moonfire", "Entangle", "Rejuvenation", "Wild Shape"],
}

@dataclass
class Character:
    name: str
    race: Race
    char_class: Class
    level: int = 1
    experience: int = 0
    health: int = 100
    mana: int = 100
    strength: int = 10
    dexterity: int = 10
    constitution: int = 10
    intelligence: int = 10
    wisdom: int = 10
    charisma: int = 10
    skills: List[str] = field(default_factory=list)
    
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
    
    def take_damage(self, amount: int):
        self.health -= amount
        return self.health <= 0
    
    def heal(self, amount: int):
        self.health = min(self.health + amount, 100)

class Adventure:
    def __init__(self, character: Character):
        self.character = character
        self.current_location = "Valley of the Four Winds"
        self.game_over = False
        self.story_progress = 0
    
    def display_status(self):
        print(f"\n{'='*50}")
        print(f"Character: {self.character.name}")
        print(f"Health: {self.character.health}/100 | Mana: {self.character.mana}/100")
        print(f"Location: {self.current_location}")
        print(f"Level: {self.character.level} | Experience: {self.character.experience}/1000")
        print(f"{'='*50}")
    
    def encounter_enemy(self):
        enemies = ["Hozen", "Sha Spawn", "Quillen", "Local Brigand"]
        enemy = random.choice(enemies)
        enemy_health = random.randint(20, 50)
        
        print(f"\n⚔️ A wild {enemy} appears!")
        
        while enemy_health > 0 and self.character.health > 0:
            print(f"\n{enemy} Health: {enemy_health}")
            print("1. Attack")
            print("2. Use Ability")
            print("3. Run Away")
            
            choice = input("Choose action: ").strip()
            
            if choice == "1":
                damage = random.randint(10, 25)
                enemy_health -= damage
                print(f"✓ You dealt {damage} damage!")
            
            elif choice == "2":
                if self.character.mana >= 20:
                    damage = random.randint(20, 35)
                    enemy_health -= damage
                    self.character.mana -= 20
                    print(f"✓ Ability used! {damage} damage dealt!")
                else:
                    print("✗ Not enough mana!")
                    continue
            
            elif choice == "3":
                print("You fled from combat!")
                return
            
            if enemy_health > 0:
                enemy_damage = random.randint(5, 15)
                if self.character.take_damage(enemy_damage):
                    print(f"✗ {enemy} dealt {enemy_damage} damage!")
                    print("☠️ You have been defeated!")
                    self.game_over = True
                    return
                else:
                    print(f"✗ {enemy} dealt {enemy_damage} damage!")
        
        if enemy_health <= 0:
            reward = random.randint(50, 150)
            self.character.gain_experience(reward)
            print(f"\n✓ Victory! Gained {reward} experience!")
    
    def explore(self):
        locations = {
            "1": ("Valley of the Four Winds", "A lush valley filled with farmland and gentle streams."),
            "2": ("Kun-Lai Summit", "Snow-capped mountains with ancient temples."),
            "3": ("Townlong Steppes", "Vast grasslands inhabited by the Yaungol."),
            "4": ("Dread Wastes", "A toxic region corrupted by the Sha."),
            "5": ("Isle of Thunder", "A mysterious island from another realm."),
        }
        
        print("\nWhere would you like to explore?")
        for key, (loc, _) in locations.items():
            print(f"{key}. {loc}")
        
        choice = input("Choose location: ").strip()
        
        if choice in locations:
            location, description = locations[choice]
            self.current_location = location
            print(f"\n📍 You arrive at {location}")
            print(f"   {description}")
            
            if random.random() > 0.5:
                print("\nYou sense danger nearby...")
                self.encounter_enemy()
            else:
                print("\nThe area is peaceful. You rest here.")
                self.character.heal(20)
                self.character.mana = min(self.character.mana + 30, 100)
    
    def visit_inn(self):
        print("\n🏨 Welcome to the Inn!")
        print("1. Rest (Recover 50 HP and 50 Mana) - 10 Gold")
        print("2. Hear Rumors")
        print("3. Leave")
        
        choice = input("What will you do? ").strip()
        
        if choice == "1":
            self.character.heal(50)
            self.character.mana = min(self.character.mana + 50, 100)
            print("✓ You feel refreshed!")
        elif choice == "2":
            rumors = [
                "Whispers speak of an ancient artifact hidden in the Dread Wastes...",
                "The Yaungol have been acting strangely near Townlong Steppes...",
                "Adventurers are needed to defend against the Sha corruption!",
            ]
            print(f"📖 {random.choice(rumors)}")
    
    def play(self):
        print(f"\n✨ Welcome to Pandaria, {self.character.name}!")
        print("Your adventure begins in the Valley of the Four Winds...\n")
        
        while not self.game_over:
            self.display_status()
            print("\nWhat would you like to do?")
            print("1. Explore")
            print("2. Visit Inn")
            print("3. Check Inventory")
            print("4. End Adventure")
            
            choice = input("Choose action: ").strip()
            
            if choice == "1":
                self.explore()
            elif choice == "2":
                self.visit_inn()
            elif choice == "3":
                print(f"\nInventory: {self.character}")
            elif choice == "4":
                print(f"\n✓ {self.character.name} returns home safely!")
                print(f"Final Stats - Level: {self.character.level}, Experience: {self.character.experience}")
                break
            else:
                print("Invalid choice. Try again.")
        
        if self.game_over:
            print("\n💀 Game Over! Return to the inn and try again.")

class CharacterCreator:
    def __init__(self):
        self.characters: List[Character] = []
    
    def create_character(self, name: str, race: Race, char_class: Class) -> Character:
        char = Character(name, race, char_class)
        
        # Apply racial bonuses
        race_bonus = RACE_ATTRIBUTES[race]
        char.strength += race_bonus["strength"]
        char.dexterity += race_bonus["dexterity"]
        char.constitution += race_bonus["constitution"]
        char.intelligence += race_bonus["intelligence"]
        char.wisdom += race_bonus["wisdom"]
        char.charisma += race_bonus["charisma"]
        
        # Assign class skills
        char.skills = CLASS_SKILLS[char_class].copy()
        
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

def display_character_details(char: Character):
    print(f"\n{'='*50}")
    print(f"Character: {char.name}")
    print(f"Race: {char.race.value} | Class: {char.char_class.value}")
    print(f"\nAttributes:")
    print(f"  Strength: {char.strength} | Dexterity: {char.dexterity}")
    print(f"  Constitution: {char.constitution} | Intelligence: {char.intelligence}")
    print(f"  Wisdom: {char.wisdom} | Charisma: {char.charisma}")
    print(f"\nSkills: {', '.join(char.skills)}")
    print(f"{'='*50}\n")

if __name__ == "__main__":
    creator = CharacterCreator()
    
    while True:
        print("\n=== Character Creator ===")
        print("1. Create Character")
        print("2. List Characters")
        print("3. Play Adventure")
        print("4. Delete Character")
        print("5. Exit")
        
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
            display_character_details(char)
        
        elif choice == "2":
            chars = creator.list_characters()
            if chars:
                print("\nCharacters:")
                for i, char in enumerate(chars, 1):
                    print(f"  {i}. {char}")
            else:
                print("No characters created yet.")
        
        elif choice == "3":
            chars = creator.list_characters()
            if chars:
                print("\nSelect a character to play:")
                for i, char in enumerate(chars, 1):
                    print(f"  {i}. {char}")
                char_choice = input("Choose character (number): ").strip()
                try:
                    char_index = int(char_choice) - 1
                    if 0 <= char_index < len(chars):
                        adventure = Adventure(chars[char_index])
                        adventure.play()
                    else:
                        print("Invalid selection.")
                except ValueError:
                    print("Invalid input.")
            else:
                print("No characters to play yet. Create one first!")
        
        elif choice == "4":
            name = input("Enter character name to delete: ").strip()
            if creator.delete_character(name):
                print(f"✓ Deleted {name}")
            else:
                print(f"✗ Character '{name}' not found")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Try again.")