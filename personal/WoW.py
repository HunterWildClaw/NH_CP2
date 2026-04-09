from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict
import random



def visit_marketplace(self):
    """Buy weapons and armor from the marketplace"""
    print("\n🏪 Welcome to the Marketplace!")
    print("=" * 50)
    
    print("Available Weapons:")
    for weapon, details in WEAPONS.items():
        print(f"{weapon} - Cost: {details['cost']} Gold, Damage: {details['damage']}, Rarity: {details['rarity']}")
    
    print("\nAvailable Armor:")
    for armor, details in ARMOR.items():
        print(f"{armor} - Cost: {details['cost']} Gold, Defense: {details['defense']}, Rarity: {details['rarity']}")
    
    print(f"{len(WEAPONS) + len(ARMOR) + 1}. Leave Marketplace")
    
    choice = input("Select item to buy (number): ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(WEAPONS) + len(ARMOR):
        item_index = int(choice) - 1
        if item_index < len(WEAPONS):
            item_name = list(WEAPONS.keys())[item_index]
            item_details = WEAPONS[item_name]
        else:
            item_index -= len(WEAPONS)
            item_name = list(ARMOR.keys())[item_index]
            item_details = ARMOR[item_name]
        
        if self.gold >= item_details["cost"]:
            self.gold -= item_details["cost"]
            self.character.add_item({"name": item_name, "rarity": item_details["rarity"], "value": item_details["cost"]})
            print(f"✓ Bought {item_name} for {item_details['cost']} Gold!")
        else:
            print("✗ Not enough gold!")
    else:
        print("Safe trading!")
    
    print("=" * 50)

def explore(self):
    unlocked_locations = self.get_unlocked_locations()
    
    print("\nWhere would you like to explore?")
    for key, (loc, _, level_req) in unlocked_locations.items():
        print(f"{key}. {loc} (Level {level_req}+)")
    
    choice = input("Choose location: ").strip()
    
    if choice in unlocked_locations:
        location, description, _ = unlocked_locations[choice]
        self.current_location = location
        print(f"\n📍 You arrive at {location}")
        print(f"   {description}")
        
        # Check for boss
        if location in ZONE_BOSSES and not self.boss_defeated.get(location, False):
            print(f"\n⚠️  You sense a powerful presence... {ZONE_BOSSES[location]['name']} lurks here!")
        
        if random.random() > 0.5:
            print("\nYou sense danger nearby...")
            self.encounter_enemy()
        else:
            print("\nThe area is peaceful. You rest here.")
            self.character.heal(20)
            self.character.mana = min(self.character.mana + 30, 100)
    else:
        print("Invalid location or not yet unlocked.")
    
    # Heal character when not in combat
    self.character.heal(10)
    self.character.mana = min(self.character.mana + 10, 100)


def level_up(self):
    self.level += 1
    self.experience = 0
    self.max_health = getattr(self, 'max_health', 100) + 50
    self.max_mana = getattr(self, 'max_mana', 100) + 50
    self.health = self.max_health
    self.mana = self.max_mana

def unlock_skills(self):
    """Unlock new skills based on character level"""
    base_skills = CLASS_SKILLS[self.char_class]
    skill_unlock_thresholds = {
        1: 0,  # All base skills available at level 1
        2: 1,  # First skill unlocked at level 2
        3: 2,  # Second skill unlocked at level 3
        4: 3,  # Third skill unlocked at level 4
        5: 4,  # All skills unlocked at level 5
    }
    
    max_skill_index = skill_unlock_thresholds.get(self.level, len(base_skills) - 1)
    self.skills = base_skills[:max_skill_index + 1]

# New mobs and loot for higher level zones
NEW_ENEMIES = {
    "Kun-Lai Summit": [
        {"name": "Snow Beast", "health": 80, "damage_range": (15, 30), "drops": [
            {"name": "Frosted Fang", "rarity": "rare", "value": 100},
            {"name": "Ice Crystal", "rarity": "common", "value": 50},
        ]},
        {"name": "Mountain Yeti", "health": 100, "damage_range": (20, 35), "drops": [
            {"name": "Yeti Pelt", "rarity": "rare", "value": 120},
            {"name": "Yeti Claw", "rarity": "common", "value": 60},
        ]},
    ],
    "Dread Wastes": [
        {"name": "Corrupted Warlord", "health": 120, "damage_range": (25, 40), "drops": [
            {"name": "Warlord's Blade", "rarity": "epic", "value": 250},
            {"name": "Corrupted Essence", "rarity": "rare", "value": 150},
        ]},
        {"name": "Sha Beast", "health": 150, "damage_range": (30, 50), "drops": [
            {"name": "Sha Heart", "rarity": "epic", "value": 300},
            {"name": "Dark Energy", "rarity": "rare", "value": 200},
        ]},
    ],
}

def get_new_enemies(self):
    """Return new enemies based on the current location."""
    return NEW_ENEMIES.get(self.current_location, [])

# Modify the encounter_enemy method to include new enemies
def encounter_enemy(self):
    enemies = get_new_enemies()
    if not enemies:
        enemies = ["Hozen", "Sha Spawn", "Quillen", "Local Brigand"]
    
    enemy = random.choice(enemies)
    enemy_health = enemy["health"]
    
    print(f"\n⚔️ A wild {enemy['name']} appears!")
    
    while enemy_health > 0 and self.character.health > 0:
        print(f"\n{enemy['name']} Health: {enemy_health}")
        self.character.display_skills()  # Show skills and health/mana
        print("1. Attack")
        print("2. Use Ability")
        print("3. Run Away")
        
        choice = input("Choose action: ").strip()
        
        if choice == "1":
            damage = random.randint(10, 25)
            enemy_health -= damage
            print(f"✓ You dealt {damage} damage!")
        
        elif choice == "2":
            if self.character.skills:
                self.character.display_skills()  # Show skills before using
                skill_choice = input("Choose skill number: ").strip()
                try:
                    skill_index = int(skill_choice) - 1
                    if 0 <= skill_index < len(self.character.skills):
                        skill_name = self.character.skills[skill_index]
                        if self.character.mana >= 20:  # Assuming all skills cost 20 mana
                            damage = random.randint(20, 35)
                            enemy_health -= damage
                            self.character.mana -= 20
                            print(f"✓ Ability '{skill_name}' used! {damage} damage dealt!")
                        else:
                            print("✗ Not enough mana!")
                            continue
                    else:
                        print("Invalid skill number.")
                except ValueError:
                    print("Invalid input.")
                continue
            
            else:
                print("✗ No skills available!")
                continue
        
        elif choice == "3":
            print("You fled from combat!")
            return
        
        if enemy_health > 0:
            enemy_damage = random.randint(*enemy["damage_range"])
            if self.character.take_damage(enemy_damage):
                print(f"✗ {enemy['name']} dealt {enemy_damage} damage!")
                print("☠️ You have been defeated!")
                self.game_over = True
                return
            else:
                print(f"✗ {enemy['name']} dealt {enemy_damage} damage!")
    
    if enemy_health <= 0:
        reward = random.randint(50, 150)
        self.character.gain_experience(reward)
        self.character.unlock_skills()  # Check for skill unlocks after combat
        # Drop items
        drops = enemy["drops"]
        if drops:
            dropped_item = random.choice(drops)
            self.character.add_item(dropped_item)
            rarity_color = "🟡" if dropped_item["rarity"] == "common" else "⭐"
            print(f"{rarity_color} {enemy['name']} dropped: {dropped_item['name']}")

def display_skills(self):
    """Display available skills and current health/mana."""
    print("Available Skills:")
    for i, skill in enumerate(self.skills, 1):
        print(f"{i}. {skill}")
    print(f"Current Health: {self.health}/100 | Current Mana: {self.mana}/100")

# Modify the encounter_enemy method to show skills
def encounter_enemy(self):
    enemies = ["Hozen", "Sha Spawn", "Quillen", "Local Brigand"]
    enemy = random.choice(enemies)
    enemy_health = random.randint(20, 50)
    
    print(f"\n⚔️ A wild {enemy} appears!")
    
    while enemy_health > 0 and self.character.health > 0:
        print(f"\n{enemy} Health: {enemy_health}")
        self.character.display_skills()  # Show skills and health/mana
        print("1. Attack")
        print("2. Use Ability")
        print("3. Run Away")
        
        choice = input("Choose action: ").strip()
        
        if choice == "1":
            damage = random.randint(10, 25)
            enemy_health -= damage
            print(f"✓ You dealt {damage} damage!")
        
        elif choice == "2":
            if self.character.skills:
                self.character.display_skills()  # Show skills before using
                skill_choice = input("Choose skill number: ").strip()
                try:
                    skill_index = int(skill_choice) - 1
                    if 0 <= skill_index < len(self.character.skills):
                        skill_name = self.character.skills[skill_index]
                        if self.character.mana >= 20:  # Assuming all skills cost 20 mana
                            damage = random.randint(20, 35)
                            enemy_health -= damage
                            self.character.mana -= 20
                            print(f"✓ Ability '{skill_name}' used! {damage} damage dealt!")
                        else:
                            print("✗ Not enough mana!")
                            continue
                    else:
                        print("Invalid skill number.")
                except ValueError:
                    print("Invalid input.")
                continue
            
            else:
                print("✗ No skills available!")
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
        self.character.unlock_skills()  # Check for skill unlocks after combat
        print(f"\n✓ Victory! Gained {reward} experience!")

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

# Item drops by enemy
ENEMY_DROPS = {
    "Hozen": [
        {"name": "Hozen Fist Weapon", "rarity": "common", "value": 10},
        {"name": "Hozen Pelt", "rarity": "common", "value": 5},
        {"name": "Banana", "rarity": "common", "value": 2},
        {"name": "Ancient Hozen Artifact", "rarity": "rare", "value": 50},
    ],
    "Sha Spawn": [
        {"name": "Sha Fragment", "rarity": "common", "value": 15},
        {"name": "Corrupted Energy", "rarity": "common", "value": 8},
        {"name": "Essence of Shadows", "rarity": "rare", "value": 60},
    ],
    "Quillen": [
        {"name": "Quillen Hide", "rarity": "common", "value": 12},
        {"name": "Quillen Spine", "rarity": "common", "value": 8},
        {"name": "Majestic Quillen Horn", "rarity": "rare", "value": 45},
    ],
    "Local Brigand": [
        {"name": "Stolen Coin Purse", "rarity": "common", "value": 20},
        {"name": "Torn Map", "rarity": "common", "value": 10},
        {"name": "Brigand's Dagger", "rarity": "rare", "value": 40},
        {"name": "Treasure Map", "rarity": "rare", "value": 100},
    ],
}

# Boss encounters
ZONE_BOSSES = {
    "Valley of the Four Winds": {
        "name": "Hozen King",
        "health": 150,
        "damage_range": (15, 30),
        "rarity": "rare",
    },
    "Kun-Lai Summit": {
        "name": "Frost Wraith",
        "health": 200,
        "damage_range": (20, 40),
        "rarity": "rare",
    },
    "Townlong Steppes": {
        "name": "Yaungol Warlord",
        "health": 180,
        "damage_range": (18, 35),
        "rarity": "rare",
    },
    "Dread Wastes": {
        "name": "Sha Lord",
        "health": 250,
        "damage_range": (25, 50),
        "rarity": "epic",
    },
    "Isle of Thunder": {
        "name": "Thunder Titan",
        "health": 300,
        "damage_range": (30, 60),
        "rarity": "epic",
    },
}

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
class Quest:
    id: int
    title: str
    description: str
    required_item: str = ""
    required_boss: str = ""
    reward_gold: int = 0
    reward_exp: int = 0
    completed: bool = False

@dataclass
class Character:
    name: str
    race: Race
    char_class: Class
    level: int = 1
    experience: int = 0
    health: int = 100
    mana: int = 100
    max_health: int = 100
    max_mana: int = 100
    strength: int = 10
    dexterity: int = 10
    constitution: int = 10
    intelligence: int = 10
    wisdom: int = 10
    charisma: int = 10
    skills: List[str] = field(default_factory=list)
    inventory: List[Dict] = field(default_factory=list)
    
    def __str__(self):
        return f"{self.name} - {self.race.value} {self.char_class.value} (Level {self.level})"
    
    def gain_experience(self, amount: int):
        self.experience += amount
        if self.experience >= 1000:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.experience = 0
        self.max_health += 50
        self.max_mana += 50
        self.health = self.max_health
        self.mana = self.max_mana
    
    def take_damage(self, amount: int):
        self.health -= amount
        return self.health <= 0
    
    def heal(self, amount: int):
        self.health = min(self.health + amount, 100)
    
    def add_item(self, item: Dict):
        self.inventory.append(item)

WEAPONS = {
    "Iron Sword": {"cost": 50, "damage": 5, "rarity": "common"},
    "Steel Mace": {"cost": 75, "damage": 10, "rarity": "common"},
    "Enchanted Bow": {"cost": 100, "damage": 15, "rarity": "rare"},
    "Flaming Axe": {"cost": 150, "damage": 25, "rarity": "rare"},
    "Shardblade": {"cost": 300, "damage": 50, "rarity": "epic"},
}

ARMOR = {
    "Leather Armor": {"cost": 40, "defense": 3, "rarity": "common"},
    "Iron Plate": {"cost": 80, "defense": 7, "rarity": "common"},
    "Steel Chainmail": {"cost": 120, "defense": 10, "rarity": "rare"},
    "Enchanted Robes": {"cost": 150, "defense": 12, "rarity": "rare"},
    "Dragon Scale Armor": {"cost": 300, "defense": 20, "rarity": "epic"},
}


class Adventure:
    LOCATIONS = {
        "1": ("Valley of the Four Winds", "A lush valley filled with farmland and gentle streams.", 1),
        "2": ("Kun-Lai Summit", "Snow-capped mountains with ancient temples.", 2),
        "3": ("Townlong Steppes", "Vast grasslands inhabited by the Yaungol.", 3),
        "4": ("Dread Wastes", "A toxic region corrupted by the Sha.", 4),
        "5": ("Isle of Thunder", "A mysterious island from another realm.", 5),
    }
    
    def __init__(self, character: Character):
        self.character = character
        self.current_location = "Valley of the Four Winds"
        self.game_over = False
        self.story_progress = 0
        self.active_quests: List[Quest] = []
        self.quest_counter = 0
        self.gold = 0
        self.boss_defeated = {}  # Track defeated bosses
    
    def display_status(self):
        print(f"\n{'='*50}")
        print(f"Character: {self.character.name}")
        print(f"Health: {self.character.health}/100 | Mana: {self.character.mana}/100")
        print(f"Location: {self.current_location}")
        print(f"Level: {self.character.level} | Experience: {self.character.experience}/1000")
        print(f"Gold: {self.gold} | Inventory Items: {len(self.character.inventory)}")
        print(f"{'='*50}")
    
    def get_unlocked_locations(self) -> dict:
        """Return only locations unlocked by current level"""
        unlocked = {}
        for key, (name, desc, level_req) in self.LOCATIONS.items():
            if self.character.level >= level_req:
                unlocked[key] = (name, desc, level_req)
        return unlocked
    
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
            
            if self.character.level > self.story_progress:
                self.story_progress = self.character.level
                print(f"\n🎉 LEVEL UP! You are now level {self.character.level}!")
                unlocked = self.get_unlocked_locations()
                if len(unlocked) > self.character.level - 1:
                    print(f"🗺️  New area unlocked!")
            
            # Drop items
            drops = ENEMY_DROPS.get(enemy, [])
            if drops:
                dropped_item = random.choice(drops)
                self.character.add_item(dropped_item)
                rarity_color = "🟡" if dropped_item["rarity"] == "common" else "⭐"
                print(f"{rarity_color} {enemy} dropped: {dropped_item['name']}")
    
    def encounter_boss(self):
        """Boss encounter in current location"""
        if self.current_location not in ZONE_BOSSES:
            print("No boss in this location.")
            return
        
        boss_data = ZONE_BOSSES[self.current_location]
        boss_name = boss_data["name"]
        boss_health = boss_data["health"]
        
        if self.boss_defeated.get(self.current_location, False):
            print(f"The {boss_name} has already been defeated.")
            return
        
        print(f"\n👹 BOSS ENCOUNTER: {boss_name}!")
        print(f"Health: {boss_health}")
        
        while boss_health > 0 and self.character.health > 0:
            print(f"\n{boss_name} Health: {boss_health}")
            print("1. Attack")
            print("2. Use Ability")
            print("3. Try to Flee")
            
            choice = input("Choose action: ").strip()
            
            if choice == "1":
                damage = random.randint(15, 30)
                boss_health -= damage
                print(f"✓ You dealt {damage} damage!")
            
            elif choice == "2":
                if self.character.mana >= 30:
                    damage = random.randint(30, 50)
                    boss_health -= damage
                    self.character.mana -= 30
                    print(f"✓ Powerful ability used! {damage} damage dealt!")
                else:
                    print("✗ Not enough mana!")
                    continue
            
            elif choice == "3":
                if random.random() > 0.3:
                    print("You managed to escape!")
                    return
                else:
                    print("Boss blocks your escape!")
            
            if boss_health > 0:
                boss_damage = random.randint(*boss_data["damage_range"])
                if self.character.take_damage(boss_damage):
                    print(f"✗ {boss_name} dealt {boss_damage} damage!")
                    print("☠️ You have been defeated by the boss!")
                    self.game_over = True
                    return
                else:
                    print(f"✗ {boss_name} dealt {boss_damage} damage!")
        
        if boss_health <= 0:
            self.boss_defeated[self.current_location] = True
            reward_exp = random.randint(300, 500)
            reward_gold = random.randint(100, 250)
            
            self.character.gain_experience(reward_exp)
            self.gold += reward_gold
            
            print(f"\n✓ BOSS DEFEATED!")
            print(f"✓ Gained {reward_exp} experience!")
            print(f"✓ Gained {reward_gold} gold!")
            
            # Boss drops rare item
            boss_item = {
                "name": f"{boss_name}'s Essence",
                "rarity": boss_data["rarity"],
                "value": reward_gold // 2
            }
            self.character.add_item(boss_item)
            rarity_icon = "⭐" if boss_data["rarity"] == "epic" else "🟡"
            print(f"{rarity_icon} Obtained: {boss_item['name']}")
    
    def explore(self):
        unlocked_locations = self.get_unlocked_locations()
        
        print("\nWhere would you like to explore?")
        for key, (loc, _, level_req) in unlocked_locations.items():
            print(f"{key}. {loc} (Level {level_req}+)")
        
        choice = input("Choose location: ").strip()
        
        if choice in unlocked_locations:
            location, description, _ = unlocked_locations[choice]
            self.current_location = location
            print(f"\n📍 You arrive at {location}")
            print(f"   {description}")
            
            # Check for boss
            if location in ZONE_BOSSES and not self.boss_defeated.get(location, False):
                print(f"\n⚠️  You sense a powerful presence... {ZONE_BOSSES[location]['name']} lurks here!")
            
            if random.random() > 0.5:
                print("\nYou sense danger nearby...")
                self.encounter_enemy()
            else:
                print("\nThe area is peaceful. You rest here.")
                self.character.heal(20)
                self.character.mana = min(self.character.mana + 30, 100)
        else:
            print("Invalid location or not yet unlocked.")
    
    def generate_quest(self):
        """Generate a random quest (collection or boss)"""
        self.quest_counter += 1
        
        # Random chance for boss quest
        if random.random() > 0.6 and self.character.level >= 2:
            boss_quests = [
                {
                    "title": f"Defeat {ZONE_BOSSES['Kun-Lai Summit']['name']}",
                    "description": "A fearsome boss terrorizes Kun-Lai Summit.",
                    "boss": "Kun-Lai Summit",
                    "reward": 150
                },
                {
                    "title": f"Defeat {ZONE_BOSSES['Dread Wastes']['name']}",
                    "description": "The Sha corruption grows stronger in the Dread Wastes.",
                    "boss": "Dread Wastes",
                    "reward": 200
                },
            ]
            template = random.choice(boss_quests)
            quest = Quest(
                id=self.quest_counter,
                title=template["title"],
                description=template["description"],
                required_boss=template["boss"],
                reward_gold=template["reward"],
                reward_exp=200
            )
        else:
            quest_templates = [
                {
                    "title": "Gather Hozen Pelts",
                    "description": "The cook needs Hozen Pelts for a special dish.",
                    "item": "Hozen Pelt",
                    "reward": 50
                },
                {
                    "title": "Collect Sha Fragments",
                    "description": "A scholar needs Sha Fragments for research.",
                    "item": "Sha Fragment",
                    "reward": 75
                },
                {
                    "title": "Find Quillen Spines",
                    "description": "A craftsperson needs Quillen Spines for armor.",
                    "item": "Quillen Spine",
                    "reward": 60
                },
                {
                    "title": "Retrieve Stolen Coin Purses",
                    "description": "Help return stolen coin purses to their owners.",
                    "item": "Stolen Coin Purse",
                    "reward": 80
                },
                {
                    "title": "Gather Ancient Artifacts",
                    "description": "A collector seeks rare ancient Hozen artifacts.",
                    "item": "Ancient Hozen Artifact",
                    "reward": 100
                },
                {
                    "title": "Collect Corrupted Energy",
                    "description": "A mage needs Corrupted Energy for experiments.",
                    "item": "Corrupted Energy",
                    "reward": 70
                },
                {
                    "title": "Find Brigand's Daggers",
                    "description": "A blacksmith wants to study Brigand's Daggers.",
                    "item": "Brigand's Dagger",
                    "reward": 90
                },
                {
                    "title": "Secure Treasure Maps",
                    "description": "A merchant pays well for Treasure Maps.",
                    "item": "Treasure Map",
                    "reward": 120
                },
            ]
            
            template = random.choice(quest_templates)
            quest = Quest(
                id=self.quest_counter,
                title=template["title"],
                description=template["description"],
                required_item=template["item"],
                reward_gold=template["reward"],
                reward_exp=100
            )
        
        self.active_quests.append(quest)
        return quest
    
    def visit_marketplace(self):
        """Sell items from inventory"""
        print("\n🏪 Welcome to the Marketplace!")
        print("=" * 50)
        
        if not self.character.inventory:
            print("Your inventory is empty. Nothing to sell!")
            print("=" * 50)
            return
        
        print("Items for Sale:")
        for i, item in enumerate(self.character.inventory, 1):
            rarity_icon = "🟡" if item["rarity"] == "common" else "⭐"
            print(f"{i}. {rarity_icon} {item['name']} - {item['value']} Gold")
        
        print(f"{len(self.character.inventory) + 1}. Leave Marketplace")
        
        choice = input("Select item to sell (number): ").strip()
        
        try:
            idx = int(choice) - 1
            if idx == len(self.character.inventory):
                print("Safe trading!")
                return
            
            if 0 <= idx < len(self.character.inventory):
                item = self.character.inventory[idx]
                self.gold += item["value"]
                self.character.inventory.pop(idx)
                print(f"✓ Sold {item['name']} for {item['value']} Gold!")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")
        
        print("=" * 50)
    
    def visit_inn(self):
        print("\n🏨 Welcome to the Inn!")
        print("1. Rest (Recover 50 HP and 50 Mana)")
        print("2. Hear Rumors")
        print("3. Accept Quest")
        print("4. Complete Quest")
        print("5. Leave")
        
        choice = input("What will you do? ").strip()
        
        if choice == "1":
            self.character.heal(50)
            self.character.mana = min(self.character.mana + 50, 100)
            self.gold -= 10 if self.gold >= 10 else 0
            print("✓ You feel refreshed!")
        
        elif choice == "2":
            rumors = [
                "Whispers speak of an ancient artifact hidden in the Dread Wastes...",
                "The Yaungol have been acting strangely near Townlong Steppes...",
                "Adventurers are needed to defend against the Sha corruption!",
                "They say the Isle of Thunder holds great treasures...",
                "Local brigands have been spotted near Kun-Lai Summit...",
            ]
            print(f"📖 {random.choice(rumors)}")
        
        elif choice == "3":
            quest = self.generate_quest()
            print(f"\n📜 New Quest Available!")
            print(f"Title: {quest.title}")
            print(f"Description: {quest.description}")
            if quest.required_item:
                print(f"Required Item: {quest.required_item}")
            if quest.required_boss:
                print(f"Required Boss: {quest.required_boss}")
            print(f"Reward: {quest.reward_gold} Gold + {quest.reward_exp} XP")
        
        elif choice == "4":
            if not self.active_quests:
                print("You have no active quests.")
                return
            
            print("\nYour Active Quests:")
            for i, quest in enumerate(self.active_quests, 1):
                status = "✓ Complete" if quest.completed else "✗ Incomplete"
                print(f"{i}. {quest.title} - {status}")
            
            quest_choice = input("Which quest to complete? ").strip()
            try:
                quest_idx = int(quest_choice) - 1
                if 0 <= quest_idx < len(self.active_quests):
                    quest = self.active_quests[quest_idx]
                    
                    # Check item quests
                    if quest.required_item:
                        has_item = any(item["name"] == quest.required_item for item in self.character.inventory)
                        if has_item:
                            self.character.inventory = [
                                item for item in self.character.inventory 
                                if item["name"] != quest.required_item
                            ]
                            self.gold += quest.reward_gold
                            self.character.gain_experience(quest.reward_exp)
                            self.active_quests.remove(quest)
                            print(f"\n✓ Quest Complete: {quest.title}")
                            print(f"✓ Received {quest.reward_gold} Gold and {quest.reward_exp} XP!")
                        else:
                            print(f"✗ You don't have {quest.required_item}!")
                    
                    # Check boss quests
                    elif quest.required_boss:
                        if self.boss_defeated.get(quest.required_boss, False):
                            self.gold += quest.reward_gold
                            self.character.gain_experience(quest.reward_exp)
                            self.active_quests.remove(quest)
                            print(f"\n✓ Quest Complete: {quest.title}")
                            print(f"✓ Received {quest.reward_gold} Gold and {quest.reward_exp} XP!")
                        else:
                            print(f"✗ You haven't defeated the required boss yet!")
            except (ValueError, IndexError):
                print("Invalid selection.")
        
        elif choice == "5":
            print("Safe travels!")
    
    def play(self):
        print(f"\n✨ Welcome to Pandaria, {self.character.name}!✨")
        print("Your adventure begins in the Valley of the Four Winds...\n")
        
        while not self.game_over:
            self.display_status()
            print("\nWhat would you like to do?")
            print("1. Explore")
            print("2. Visit Inn")
            print("3. Visit Marketplace")
            print("4. Challenge Boss")
            print("5. Check Inventory")
            print("6. View Quests")
            print("7. End Adventure")
            
            choice = input("Choose action: ").strip()
            
            if choice == "1":
                self.explore()
            elif choice == "2":
                self.visit_inn()
            elif choice == "3":
                self.visit_marketplace()
            elif choice == "4":
                self.encounter_boss()
            elif choice == "5":
                self.display_inventory()
            elif choice == "6":
                self.display_quests()
            elif choice == "7":
                print(f"\n✓ {self.character.name} returns home safely!")
                print(f"Final Stats - Level: {self.character.level}, Experience: {self.character.experience}")
                print(f"Gold Earned: {self.gold}")
                break
            else:
                print("Invalid choice. Try again.")
        
        if self.game_over:
            print("\n💀 Game Over! Return to the inn and try again.")
    
    def display_inventory(self):
        print(f"\n{'='*50}")
        print("INVENTORY")
        print(f"{'='*50}")
        if self.character.inventory:
            total_value = 0
            for i, item in enumerate(self.character.inventory, 1):
                rarity_icon = "🟡" if item["rarity"] == "common" else "⭐"
                print(f"{i}. {rarity_icon} {item['name']} (Value: {item['value']} Gold)")
                total_value += item["value"]
            print(f"\nTotal Inventory Value: {total_value} Gold")
        else:
            print("Your inventory is empty.")
        print(f"{'='*50}\n")
    
    def display_quests(self):
        print(f"\n{'='*50}")
        print("ACTIVE QUESTS")
        print(f"{'='*50}")
        if self.active_quests:
            for i, quest in enumerate(self.active_quests, 1):
                status = "✓" if quest.completed else "✗"
                print(f"{i}. {status} {quest.title}")
                print(f"   Description: {quest.description}")
                if quest.required_item:
                    print(f"   Need: {quest.required_item} | Reward: {quest.reward_gold} Gold + {quest.reward_exp} XP")
                if quest.required_boss:
                    print(f"   Defeat: {quest.required_boss} | Reward: {quest.reward_gold} Gold + {quest.reward_exp} XP")
        else:
            print("No active quests. Visit the inn to accept one!")
        print(f"{'='*50}\n")

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