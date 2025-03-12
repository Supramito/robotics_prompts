
# Day 8 Challenge
#I learned a new skill in coding with python

name = input("What is your name? ")
day = input("What day of the week is it? ").lower()
favorite_color = input("What is your favorite color? ")
favorite_animal = input("What is your favorite animal? ")
hobby = input("What is one hobby you enjoy? ")

print("\nGenerating your personalized affirmation...\n")


if day == "monday":
  print(f"Happy Monday, {name}! Your energy shines as bright as the color {favorite_color}. This week, embrace your {hobby} with the grace of a {favorite_animal}!")

elif day == "tuesday":
  print(f"Tuesday's here, {name}! Channel the strength of a {favorite_animal} today. Your passion for {hobby} will inspire everyone around you!")

elif day == "wednesday":
  print(f"Wonderful Wednesday, {name}! Like the beautiful shade of {favorite_color}, you bring color to everyone's life. Your {hobby} skills are developing amazingly!")

elif day == "thursday":
  print(f"It's Thursday, {name}! You have the determination of a {favorite_animal} and the vibrance of {favorite_color}. Today your {hobby} will bring you joy!")

elif day == "friday":
  print(f"Fantastic Friday, {name}! Wear your {favorite_color} proudly today. Your {hobby} passion reminds everyone of a {favorite_animal}'s enthusiasm for life!")

elif day == "saturday":
  print(f"Super Saturday, {name}! Take time to enjoy your {hobby} today. Your {favorite_color} energy and {favorite_animal}-like spirit make you unstoppable!")

elif day == "sunday":
  print(f"Serene Sunday, {name}! Reflect on your week with the wisdom of a {favorite_animal}. Your connection to {hobby} and love for {favorite_color} show your unique personality!")

else:
  print(f"I'm not sure if {day} is a valid day, {name}, but regardless, you're amazing! Keep loving {favorite_color}, {favorite_animal}s, and {hobby}!")

print("\nHave a wonderful day!")
