Red=Nathan   Green=Bennett
#NH, BHR 2nd character creator 
Import the attribute dice roller that we did for notes that one time

main menu function
	Infinite loop
		Ask the user if they want to 1. Quit 2. Create a character 3. Find a character
		If they chose 1
			Break the infinite loop
		Otherwise if they chose 2
			Call the function to create a character
		Otherwise if they chose 3
			Call the function to find a character
		Otherwise
			display an invalid attempt for input validation

Create a function for creating a character
	Infinite loop
		Display all possible races
		Ask for race
		If the race is an option
			Break the loop
		Otherwise tell them to try again
	Infinite loop
		Display all possible classes
		Ask for class
		If the class is an option
			Break the loop
		Otherwise tell them that they must try again
	Infinite loop
		Ask for name
		If that name exists
			Tell them that they must try again with a name not already used
		Otherwise if that name doesn’t even exist
			Force them to try again
		Otherwise
			End the infinite loop
	Run the attribute dice roller from last year
	Infinite loop
		Display the possible skill for the user
		Let them choose their skill
		If that skill is a valid option
			End the loop
		Otherwise tell the user that they must try again

	Infinite loop
		What is your starting level
		If it is possible and available
			End the loop
		Otherwise tell them that they need to try again

search character function
	input for viewing 1 character or comparing 2
	if user views 1 character
		input for what character (name? class? level?)
		dictionary of characters 
		if input is in the dictionary of characters
			display all available characters assigned with a number
			input for what character to view
		display all sections of the dictionary according to the digit
		end function
	elif user compares 2 characters 
input for what character (name? class? level?)
		dictionary of characters 
		if input is in the dictionary of characters
			display all available characters assigned with a number
			input for what character to view
input for 2nd character (name? class? level?)
		dictionary of characters 
		if input is in the dictionary of characters
			display all available characters assigned with a number
			input for what character to view
display all sections according to the digit such

manage inventory function
	Check if the user wants to delete, add, equip items, or quit
	if inventory dict is none (== false, doesn’t have anything in it)
			display that there’s nothing in the user’s inventory
		Otherwise if inventory weighs too much
			Display that they can’t add anything yet
			Force them to sell some items
		Otherwise
			If they want to sell items
				Show all their items by calling a function
				Let them choose which item to sell
				Give them one coin for each
			Otherwise if they want to buy items
				Infinite loop
	Show the shop in which everything is overpriced
					Let them decide what to buy
					If that is a valid option
					End the loop
				Otherwise
					Tell them to try again
		Otherwise if they want to equip items
			Infinite loop
				Display all the weapons
				Ask what weapon or armour they want to equip
				If that weapon is a valid choice
				Equip it to the character and increase stats based						on the weapon/armour
				End the loop
			Otherwise if that weapon is not a valid choice
				GGHave them try again
			Otherwise if they want to equip items
				

Display items function
	For every item
		Display it

Create a function to create a backstory
	If the character is this race
		Give a random half a prompt
	Etc.
	If the character is this class
		Give the other half of the prompt
	Etc. 
	If the character has mostly this attribute
		Fill in part of the prompt
	Otherwise if the character has mostly this attribute
		Give a different prompt
	Etc.
	Otherwise if the character has a tie between these attributes
		Give a different prompt
	Etc. 
	If the character has this skill
		Fill in the rest of the prompt
	Display the prompt to the user

call main menu function
