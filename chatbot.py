# your chatbot code here!
    
siblings = int(input("How many brothers and sisters do you have?"))

if siblings == 0:
    print("You're an only child.")
elif siblings > 5:
    print("well that's a big family!")
elif siblings > 10:
    print("wow that is an impressing amount of siblings!")

   # my bot 
   name = input("Hello, what's your name?")
print("Hello", name)

    age = int(input("How old are you?"))
if age <= 10:
    print(age, "is a great age to be!")
elif age <=18:
    print("Being", age, "can be pretty stressful sometimes :/")
elif age >=19:
    print(age , "is a good age to be!")

song = int(input("""What's your favourite music genre?
             1. Pop
             2. Jazz
             3. Rock
             4. Hip hop
             5. Country
             6. Others"""))

if song == "1":
    song = "Pop"
    print("I love pop music too!")
elif song == "2":
    song = "Jazz"
    print("I love jazz music too!")
elif song == "3":
    song = "Rock"
    print("I love rock music too!")
elif song == "4":
    song = "Hip hop"
    print("I love hip hop music too!")
elif song == "5":
    song = "Country"
    print("I love country music too!")
elif song == "6":
    song = "Others"
    print("Ooh interesting!")
