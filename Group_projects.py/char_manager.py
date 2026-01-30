#NH, BR 2nd character creator
import random


characters={}
for i in characters:
   items_in_inv=[]
   inv_weight=items_in_inv(len)
   weight_limit=1000


races = (
   {
       "name": "Elves",
       "strength_modifier": 1,
       "intelligence_modifier": 3,
       "wisdom_modifier": 2,
       "charisma_modifier": 2,
       "dexterity_modifier": 2,
       "constitution_modifier": 0,
   },
   {
       "name": "Dwarves",
       "strength_modifier": 3,
       "intelligence_modifier": -1,
       "wisdom_modifier": 2,
       "charisma_modifier": -1,
       "dexterity_modifier": 0,
       "constitution_modifier": 1,
   },
   {
       "name": "Orcs",
       "strength_modifier": 3,
       "intelligence_modifier": -2,
       "wisdom_modifier": 1,
       "charisma_modifier": -2,
       "dexterity_modifier": 2,
       "constitution_modifier": 1,
   },
   {
       "name": "Goblins",
       "strength_modifier": 0,
       "intelligence_modifier": 1,
       "wisdom_modifier": 1,
       "charisma_modifier": -1,
       "dexterity_modifier": 2,
       "constitution_modifier": 2,
   },
   {
       "name": "Halflings",
       "strength_modifier": 0,
       "intelligence_modifier": 1,
       "wisdom_modifier": 0,
       "charisma_modifier": 0,
       "dexterity_modifier": 2,
       "constitution_modifier": 1,
   },
)


classes = (
   {
   "name":"Paladin",
   "strength_modifier": 2,
   "intelligence_modifier": 1,
   "wisdom_modifier": 2,
   "charisma_modifier": 2,
   "dexterity_modifier": 1,
   "constitution_modifier": 2,
}, {
   "name":"Rogue",
   "strength_modifier": 1,
   "intelligence_modifier": 2,
   "wisdom_modifier": 1,
   "charisma_modifier": 2,
   "dexterity_modifier": 4,
   "constitution_modifier": 1,
}, {
   "name":"Monk",
   "strength_modifier": 1,
   "intelligence_modifier": 2,
   "wisdom_modifier": 2,
   "charisma_modifier": 1,
   "dexterity_modifier": 2,
   "constitution_modifier": 1,
},{
   "name":"Mage",
   "strength_modifier": -1,
   "intelligence_modifier": 4,
   "wisdom_modifier": 2,
   "charisma_modifier": 1,
   "dexterity_modifier": 0,
   "constitution_modifier": 0,
}, {
   "name":"Hunter",
   "strength_modifier": 2,
   "intelligence_modifier": 1,
   "wisdom_modifier": 2,
   "charisma_modifier": 0,
   "dexterity_modifier": 2,
   "constitution_modifier": 2,
}, {
   "name":"Warrior",
   "strength_modifier": 4,
   "intelligence_modifier": 1,
   "wisdom_modifier": 2,
   "charisma_modifier": 1,
   "dexterity_modifier": 2,
   "constitution_modifier": 3,
}, {
   "name":"Druid",
   "strength_modifier": 2,
   "intelligence_modifier": 3,
   "wisdom_modifier": 4,
   "charisma_modifier": 1,
   "dexterity_modifier": 2,
   "constitution_modifier": 3,
})


#Create a function for creating a character
def character_creator(characters, races, classes):
#   Infinite loop
   while True:
#       Display all possible races
       print("Available races:")
       for i, race in enumerate(races, 1):
           print(f"{i}. {race['name']}")
#       Ask for race
       character_race = input("What race would you like? (Enter number): ").strip()
#       If the race is a valid option
       try:
           race_index = int(character_race) - 1
           if 0 <= race_index < len(races):
#           Break the loop
               break
           else:
               print("🚫That input was invalid. Please try again.🚫")
       except ValueError:
           print("🚫That input was invalid. Please try again.🚫")
#       Otherwise tell them to try again
       print("🚫That input was invalid. Please try again. 🚫")
#   Infinite loop
   while True:
#       Display all possible classes
       print("Available classes:")
       for i, cls in enumerate(classes, 1):
           print(f"{i}. {cls['name']}")
#       Ask for class
       character_class = input("What class would you like? (Enter number): ").strip()
#       if the class is a valid option
       try:
           class_index = int(character_class) - 1
           if 0 <= class_index < len(classes):
#           Break the loop
               break
           else:
               print("🚫That input was invalid. Please try again.🚫")
       except ValueError:
           print("🚫That input was invalid. Please try again.🚫")
#   Infinite loop
   while True:
#       Ask for name
       character_name=input("What name do you want for your character? ")
#       If that name exists
       if character_name in characters:
#           Tell them that they must try again with a name not already used
           print("🚫That name already exists. Please try again.🚫")
#       Otherwise if that name doesn’t even exist
       elif character_name not in characters:
#           End the infinite loop
           break


#   Run the attribute dice roller from last year
   strength, intelligence, wisdom,  charisma, constitution, dexterity = attribute_roller(characters)
#   Infinite loop
   while True:
#       Display the possible skill for the user
       print("Your possible skills are: ")
       skills = ["Archery", "Swordsmanship", "Magic", "Stealth", "Healing", "Intimidation"]
       for i, skill in enumerate(skills, 1):
           print(f"{i}. {skill}")
#       Let them choose their skill
       character_skill = input("What skill would you like? (Enter number): ").strip()
#       If that skill is a valid option
       try:
           skill_index = int(character_skill) - 1
           if 0 <= skill_index < len(skills):
#           End the loop
               break
#       Otherwise tell the user that they must try again
           else:
               print("That input was invalid. Please try again.")
       except ValueError:
           print("That input was invalid. Please try again.")
   character_race = (int(character_race) - 1)
   for i in range(len(races)):
       if character_race == i:
           character_race = races[i]["name"]
   character_class = (int(character_class) - 1)
   for i in range(len(classes)):
       if character_class == i:
           character_class = classes[i]["name"]
   characters[character_name] = {
"race": character_race,
"class": character_class,
"strength": strength,
"intelligencer": intelligence,
"wisdom":  wisdom,
"charisma": charisma,
"dexterity": dexterity,
"constitution": constitution,
"inventory": {}
}
#search character function
def search_character(characters):
   while True:
       name = input("What is the name of your character? (or type 'quit' to leave): ").title().strip()
       if name == "Quit":
           break
       elif name in characters:
           print(characters[name])
           break
       else:
           print("That was not a name in the list of characters.")


#manage inventory function
def manage_inventory(items_in_inv, inv_weight, weight_limit):
   while True:
       user_choice = input("Would you like to: \n1. Add an item \n2. Equip a pre-existent item \n3. Delete an item \n4. View inventory \n5. Leave inventory\nInsert number: ").strip()
       if user_choice == '1':
           if inv_weight >= weight_limit:
               print("🚫You can't add anything - inventory is full!🚫")
           else:
               item_name = input("Enter item name: ").strip()
               try:
                   item_weight = int(input("Enter item weight: ").strip())
                   if inv_weight + item_weight <= weight_limit:
                       items_in_inv.append({"name": item_name, "weight":
                       item_weight})
                       inv_weight += item_weight
                       print(f"Added {item_name}!")
                   else:
                       print("🚫Item too heavy for remaining capacity.🚫")
               except ValueError:
                   print("🚫Invalid weight input.🚫")
       elif user_choice == '2':
           if not items_in_inv:
               print("💨Nothing in inventory to equip!💨")
           else:
               for i, item in enumerate(items_in_inv, 1):
                   print(f"{i}. {item['name']} (Weight: {item['weight']})")
               try:
                   choice = int(input("Select item number: ").strip()) - 1
                   if 0 <= choice < len(items_in_inv):
                       print(f"Equipped {items_in_inv[choice]['name']}!")
                   else:
                       print("Invalid selection.")
               except ValueError:
                   print("Invalid input.")
       elif user_choice == '3':
           if not items_in_inv:
               print("💨Nothing in inventory to delete!💨")
           else:
               for i, item in enumerate(items_in_inv, 1):
                   print(f"{i}. {item['name']}")
               try:
                   choice = int(input("Select item to delete: ").strip()) - 1
                   if 0 <= choice < len(items_in_inv):
                       removed = items_in_inv.pop(choice)
                       inv_weight -= removed['weight']
                       print(f"Deleted {removed['name']}!")
                   else:
                       print("Invalid selection.")
               except ValueError:
                   print("Invalid input.")


       elif user_choice == '4':
           if not items_in_inv:
               print("💨Inventory is empty!💨")
           else:
               print("\n💰Your Inventory💰")
               for i, item in enumerate(items_in_inv, 1):
                   print(f"{i}. {item['name']} (Weight: {item['weight']})")
               print(f"Total weight: {inv_weight}/{weight_limit}\n")
     
       elif user_choice == '5':
           break
       else:
           print("🚫Invalid input. Please try again.🚫")


#Display items function
def display_items(items_in_inv):
   if not items_in_inv:
       print("🚫No items to display.🚫")
   else:
       print("\nYour Items:")
       for i, item in enumerate(items_in_inv, 1):
           print(f"{i}. {item['name']} (Weight: {item['weight']})")
       print()


def attribute_roller(characters):
   def checker(key):
       while True:
           attribute = input(f"Which roll do you want to choose for your {key}? ")
           if attribute in attribute_rolls:
               attribute_rolls.remove(attribute)
               for i in attribute_rolls:
                   print(i)
               return attribute
   attribute_rolls = []
   print("Your attribute options are: ")
   for i in range(6):
       attribute_rolls.append(str(random.randint(1,6) + random.randint(1,6) + random.randint(1,6)))
       print(attribute_rolls[i - 1])
   strength = checker("strength")
   intelligence = checker("intelligence")
   wisdom = checker("wisdom")
   dexterity = checker("dexterity")
   charisma = checker("charisma")
   constitution = checker("constitution")
   return strength, intelligence, wisdom,  charisma, constitution, dexterity


#main menu function
def main(characters, races, classes):
#   Infinite loop
   while True:
#       Ask the user if they want to 1. Quit 2. Create a character 3. Find a character
       check = input("Do you want to: \n1. Create a character \n2. Find a character \n3. Manage inventory \n4. Quit \n")
#       If they chose 1
       if check == '1':
           character_creator(characters, races, classes)
#           Call the function to create a character
#       Otherwise if they chose 2
       elif check == '2':
#           Call the function to find a character
           search_character(characters)
#       Otherwise if they chose 3
       elif check == '3':
#           Call the function to manage inventory
           items_in_inv = []
           inv_weight = 0
           weight_limit = 50
           manage_inventory(items_in_inv, inv_weight, weight_limit)
#       Otherwise if they chose 4
       elif check == '4':
#           Break the infinite loop
           break
#       Otherwise
       else:
#           display an invalid attempt for input validation
           print("🚫That was an invalid input. Please try again. 🚫")


#call main menu function
main(characters, races, classes)
