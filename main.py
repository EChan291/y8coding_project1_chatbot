
# First Bot

name = input("Hello, what's your name?")
print("Hello", name)

age = int(input("How old are you?"))
print(age, "is a great age to be!")

lesson = input("What's your favourite lesson?")
lettersoflesson = len(lesson)
print("I like", lesson, "too!")
print(lesson, "has", lettersoflesson, "letters!")

teacher = input("Who is your teacher?")
print(teacher, "makes me think too hard!")


# Second Bot

country = input("Hello, what is your country?")
first_letter = country[0]
print("Your country begins with", first_letter)
food = input("What is your favourite food?")
firstletter = food[0]
print("Your food begins with", firstletter)
print("You like to eat", food*3, "in", country)