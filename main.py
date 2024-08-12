import random

user_scores = 0
for i in range(5):
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    mult = x * y
    print(f"Problem {i + 1}: What is {x} x {y}?")
    user_input = input("Your Answer: ")
    try:
        intInput = int(user_input)
        if intInput == mult:
            user_scores += 1
            print("Correct!")
        elif intInput != mult:
            print(f"incorrect! the correct answer was {mult}")
    except:
        print("ValueError! Please input numbers")

print(f"you scored {user_scores} out of 5")