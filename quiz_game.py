print("Welcome to the Python Quiz Game!")
print("----------------------------------")

score = 0

# Question 1
answer = input("1. What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong ❌")

# Question 2
answer = input("2. Which language is used for web development? ")

if answer.lower() == "javascript":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong ❌")

# Question 3
answer = input("3. What does HTML stand for? ")

if answer.lower() == "hyper text markup language":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong ❌")

# Question 4
answer = input("4. What does CSS stand for? ")

if answer.lower() == "cascading style sheets":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong ❌")

# Question 5
answer = input("5. Python is a programming language? (yes/no) ")

if answer.lower() == "yes":
    print("Correct! ✅")
    score += 1
else:
    print("Wrong ❌")

print("----------------------------------")
print("Your final score is:", score, "/5")