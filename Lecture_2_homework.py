import random

user_scores = 0
for i in range(5):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    mult = x * y
    print(f"Problem {i + 1}: What is {x} x {y}?")
    user_input = int(input("Your Answer: "))
    if type(user_input) != int:
        print("please input a number")
    elif type(user_input) == int and user_input == mult:
        user_scores += 1
        print("Correct!")
    elif type(user_input) == int and user_input != mult:
        print(f"incorrect! the correct answer was {mult}")

print(f"you scored {user_scores} out of 5")
