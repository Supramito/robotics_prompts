#Day 9
# I learned how to make a float. Its when you make the code so that it wont crash if decimals are inputted
# Generation Generator
birthYear = int(input("What year were you born? "))

if birthYear <= 1946:
  print("You are a Traditionalist.")
elif birthYear >= 1947 and birthYear <= 1964:
  print("Hey, Baby Boomer! How you doing?")
elif birthYear >= 1965 and birthYear <= 1981:
  print("Gen X! What's up?")
elif birthYear >= 1982 and birthYear <= 1995:
  print("Millenials! The age of tech!")
elif birthYear >= 1996:
  print("Hey, Gen Z! TikTok much?")
else: 
  print("Try again!")
