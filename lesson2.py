print(""" 
      1. Typhoon
      2. Sunny
      3. Snowing
      4. Foggy
      5. Cloudy""")
weather = input("What is the weather like today?")

if weather == "1":
    location = "inside"
elif weather == "2":
    location = "at the beach"
elif weather == "3":
    location = "on a mountain"
elif weather == "4":
    location = "at home"
elif weather == "5":
    location = "at the garden"

print("""
      1. Breakfast
      2. Lunch
      3. Dinner""")
food = input("What are you eating?")

if food == "1":
    food = "breakfast"
elif food == "2":
    food = "lunch"
elif food == "3":
    food = "dinner"

print(f"Today you are {location} eating {food}!")



