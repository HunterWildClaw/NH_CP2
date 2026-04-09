# WoW: Python RPG Module ⚔️

This is a World of Warcraft-inspired RPG engine built with Python. It features a complex character system, racial attributes, class-based skills, and a dynamic exploration/combat system.

## 🕹️ Core Engine Features
- **Character Customization**: Support for 12 Races (Orc, Tauren, Pandaren, etc.) and 11 Classes (Warrior, Mage, Monk, etc.), each with unique base attributes.
- **Dynamic Combat**: Turn-based combat system with physical attacks, mana-consuming abilities, and enemy scaling.
- **Loot & Economy**: Marketplace for gear and enemy drop tables (common/rare/epic) based on the zone.
- **Exploration**: Level-locked zones including *Kun-Lai Summit* and *Dread Wastes*.
- **Quest System**: Dataclass-driven quests that track boss kills and item requirements.

## 🛠️ Technical Stack
- **Languages**: Python 3.12
- **Architecture**: Object-Oriented Programming (OOP) using `dataclasses` and `enums`.
- **UI Framework**: Transitioning from a Terminal-based logic to a `tkinter` GUI.

## 📂 Data Structure
- `Race` & `Class`: Enums for type safety.
- `Character`: The primary dataclass managing stats, inventory, and skills.
- `ZONE_BOSSES`: A dictionary mapping high-level encounters to specific geographic locations.

## 🚀 Future Roadmap
- [ ] **GUI Integration**: Porting the `print()` and `input()` terminal logic into Tkinter Text widgets and Buttons.
- [ ] **Visual Inventory**: Replacing the list-based inventory with a grid of item icons.
- [ ] **Save/Load**: Implementing `json` or `sqlite3` to save character progress.