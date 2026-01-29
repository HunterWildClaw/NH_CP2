#Red=Nathan   Green=Bennett
#NH, BHR 2nd character creator 

characters=[]

for i in characters:
    items_in_inv=[]
    inv_weight=items_in_inv(len)
    weight_limit =50

races=(
	{
	"name":"Elves",
	"strength_modifier": 1,
	"intelligence_modifier": 3,
	"wisdom_modifier": 2,
	"charisma_modifier": 2,
	"dexterity_modifier": 2,
	"constitution_modifier": 0,
}, {
	"name": "Dwarves",
	"strength_modifier": 3,
	"intelligence_modifier": -1,
	"wisdom_modifier": 2,
	"charisma_modifier": -1,
	"dexterity_modifier": 0,
	"constitution_modifier": 1,
}, {
	"name": "Orcs",
	"strength_modifier": 3,
	"intelligence_modifier": -2,
	"wisdom_modifier": 1,
	"charisma_modifier": -2,
	"dexterity_modifier": 2,
	"constitution_modifier": 1,
}, {
	"name": "Goblins",
	"strength_modifier": 0,
	"intelligence_modifier": 1,
	"wisdom_modifier": 1,
	"charisma_modifier": -1,
	"dexterity_modifier": 2,
	"constitution_modifier": 2,
}, {
	"name": "Halflings", 
	"strength_modifier": 0,
	"intelligence_modifier": 1,
	"wisdom_modifier": 0,
	"charisma_modifier": 0,
	"dexterity_modifier": 2,
	"constitution_modifier": 1,
})
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
#main menu function
def main(characters, races, classes):
#	Infinite loop
	while True:
#		Ask the user if they want to 1. Quit 2. Create a character 3. Find a character
		check = input("Do you want to: \n1. Create a character \n2. Find a character \n3. Quit \n")
#		If they chose 1
		if check == '1':
			character_creator(characters, races, classes)
#			Call the function to create a character
#		Otherwise if they chose 2
		elif check == '2':
#			Call the function to find a character
			search_character(characters)
#		Otherwise if they chose 3
		elif check == '3':
#			Break the infinite loop
			break
#		Otherwise
		else:
#			display an invalid attempt for input validation
			print("That was an invalid input. Please try again. ")

#Create a function for creating a character
def character_creator(characters, races, classes):
#	Infinite loop
    racess = []
    classess []
	while True:
#		Display all possible races
		for i in races:
			print(i["name"])
			racess.append(i["name"])
#		Ask for race
		character_race=input("What race would you like out of the available options?: ")
#		If the race is an option
		if character_race in races:
#			Break the loop
			break
#		Otherwise tell them to try again
		print("That input was invalid. Please try again. ")
#	Infinite loop
	while True:
#		Display all possible classes
		for i in races
#		Ask for class
		character_class =input("What class would you like for your ………………..character?").title().strip()
#		if the class is an option
		if character_class in classes:
#			Break the loop
			break
#		Otherwise tell them that they must try again
		elif character_class not in classes:
			print("Try again")
#	Infinite loop
	while True:
#		Ask for name
		character_name=input("What name do you want for your character?")
#		If that name exists
		if character_name in characters:
#			Tell them that they must try again with a name not already used
			print("That name already exists. Please try again.")
#		Otherwise if that name doesn’t even exist
		elif character_name not in characters:
#			End the infinite loop
			break

#	Run the attribute dice roller from last year
	
#	Infinite loop
	while True:
#		Display the possible skill for the user
		print("Your possible skills are: ")
		
#		Let them choose their skill
#		If that skill is a valid option
#			End the loop
#		Otherwise tell the user that they must try again

#search character function
def search_character(characters):
    while True:
#		input for what character (name? class? level?)
        name=input("What is the name of your character? ").title().strip()
    #		dictionary of characters 
    #		if input is in the dictionary of characters
        if name in characters:
    #		display the character’s information
            print(characters[name])
            break
        elif name not in characters:
            print("That was not a name in the list of characters. ")
            

#manage inventory function
def manage_inventory():
#	Check if the user wants to delete, add, equip items, or quit
	user_choice=input("Would you like to: \n1. Add an item \n2. Equip a pre-existent item \n3. Delete an item \n4. Leave inventory\nInsert number: ").strip()
	if user_choice=='1':
#		if inventory dict is none (== false, doesn’t have anything in it)
		if not items_in_inv:
#			display that there’s nothing in the user’s inventory
			print("Nothing in here!")
#		Otherwise if inventory weighs too much
		if inv_weight > weight_limit:
#			Display that they can’t add anything yet
			print("You can't add anything")
#			Force them to sell some items
			market_place()
#		Otherwise
#			If they want to sell items
#				Show all their items by calling a function
#				Let them choose which item to sell
#				Give them one coin for each
#			Otherwise if they want to buy items
#				Infinite loop
#	Show the shop in which everything is overpriced
	#				Let them decide what to buy
	#				If that is a valid option
#					End the loop
#				Otherwise
#					Tell them to try again
	#	Otherwise if they want to equip items
	#		Infinite loop
	#			Display all the weapons
	#			Ask what weapon or armour they want to equip
	#			If that weapon is a valid choice
#				Equip it to the character and increase stats based		#				on the weapon/armour
#				End the loop
#			Otherwise if that weapon is not a valid choice
#				Have them try again

#Display items function
#	For every item
#		Display it

#Create a function to create a backstory
#	If the character is this race
#		Give a random half a prompt
#	Etc.
#	If the character is this class
#		Give the other half of the prompt
#	Etc. 
#	If the character has mostly this attribute
#		Fill in part of the prompt
#	Otherwise if the character has mostly this attribute
#		Give a different prompt
#	Etc.
#	Otherwise if the character has a tie between these attributes
#		Give a different prompt
#	Etc. 
#	If the character has this skill
#		Fill in the rest of the prompt
#	Display the prompt to the user

def attribute_roller(characters):
	def checker(attribute):
		while True:
			attribute = input(f"Which roll do you want to choose for your {attribute}? ")
			if attribute in attribute_rolls:
				attribute_rolls.pop(attribute)
				for i in attribute_rolls:
					print(i)
				return attribute
	attribute_rolls = []
	print("Your attribute options are: ")
	for i in range(6):
		attribute_rolls.append(string(random.randint(1,6) + random.randint(1,6) + random.randint(16)))
		print(attribute_rolls[i - 1])
	strength = checker(strength)
	intelligence = checker(intelligence)
	wisdom = checker(wisdom)
	dexterity = checker(dexterity)
	charisma = checker(charisma)
	constitution = checker(constitution)

#call main menu function
main(characters, races, classes)