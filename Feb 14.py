#Today I learned how to use inputs and prints in one big sentence.

\



myName = input("What's your name? ")
myLunch = input("What are you having for lunch? ")
print(myName, "is going to be chowing down on", myLunch, "very soon!")

yourName = input("Name: ")
whatYear = input("What year is it?: ")
print(yourName, "thinks it is", whatYear)

yourName = input("Name: ")
whatYear = input("What year is it?: ")
print(yourName, "thinks it is", whatYear)


print("=== Your Song Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
song, totally copyright free 😭""")
print()
person = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person's name: ")
print()
print("There was a person called", person)
print("Who did something cool like",thing,"at the wonderful",place,  "where you'll find me", rhyme)

food = input("Name a food: ")
plant = input("Name a type of plant: ")
cookingType = input("What is a way to cook something?")
burntFood = input("How do you describe burnt food?")
householdItem = input("Name something in your house: ")
print()
print("Tonight's dinner:")
print("For dinner you should make", cookingType, food, "with", burntFood, plant, "on a plate of",householdItem)
