# First Bot

name = input("What is your name?")
print("Hello,", name,"!")
age = int(input("How old are you?"))
if age <= 10:
    print(age, "is a great age to be!")
elif age <=18:
    print("Being", age, "can be pretty stressful sometimes :/")
elif age >=19:
    print(age , "is a good age to be!")
lesson = input("What's your favourite lesson?")
lettersoflesson = len(lesson)
print("I like", lesson, "too!")
print(lesson, "has", lettersoflesson, "letters!")
teacher = input("Who is your teacher?")
print(teacher, "is a very nice teacher!")
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

# Second Bot

country = input("Hello! Where are you from?")
first_letter = country[0]
print("Oh wow!", country, "is a great place!")
print("First letter of", country,"is",first_letter)
food = input("What is your favourite food?")
firstletter = food[0]
print("I love", food, "too!")
print("Your favourite food begins with a", firstletter)
print("You like eating", food*3, "in", country)
