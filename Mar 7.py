# learned about ELIF statements.
print("SECURE LOGIN")
username = input("Username > ")
password = input("Password> ")

if username == "mark" and password == "password":
  print("Welcome Mark!")
elif username == "suzanne" and password == "Su74nne":
  print("Hey there Suzanne!")
else:
  print("Go away!")


print("SECURE LOGIN")
username = input("Username > ")

if username == "mark":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
  print("Go away!")


season = input("What is your favorite season?")
if season == "spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == "summer":
  print("Catch some sun and cool off with a lemonade.")
elif season == "autumn":
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == "winter":
  print("Stay warm by the fire and watch the snow fall.")
else: 
  print("I don't know that season. Please try again.")
