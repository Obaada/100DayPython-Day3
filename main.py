print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? " ))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else: 
    print("Please pay $12.")
else: 
  print("Sorry, you need to grow taller before you can ride.")


###############################################################################################
#check number if even or odd
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
reminder = number % 2
type = ""
if reminder > 0:
  type = "odd"
else: type = "even"

print("This is an " + type + " number.")
##############################################################################################
# BMI 2.0
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / height ** 2
result = ""
if BMI < 18.5:
  result = "are underweight"
elif BMI < 25:
  result = "have a normal weight"
elif BMI < 30: 
  result = "are slightly overweight"
elif BMI < 35:
  result = "are obese"
else:
  result = "are clinically obese"

print(f"Your BMI is {BMI}, you {result}", end=".")
##############################################################################################
# check if year is a leap year
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
answer = ""
if year % 4 == 0:
  if year % 100 != 0:
    answer = "Leap year"
  else: 
    if year % 400 == 0:
      answer = "leap year"
    else:
      answer = "Not leap year"
else: 
  answer = "Not leap year"

print(answer)
#############################################################################################
# Pizza order
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
Bill = 0
if size == "S":
  Bill += 15
if size == "M":
  Bill += 20
if size == "L": 
  Bill += 25

if add_pepperoni == "Y":
  if size == "S":
    Bill += 2
  else:
    Bill += 3

if extra_cheese == "Y":
  Bill += 1

print(f"Your final bill is: ${Bill}.")
#################################################################################################
# love calculator
print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
TRUE = 0
LOVE = 0
answer = ""
TRUE += name1.count("t") + name2.count("t")
TRUE += name1.count("r") + name2.count("r")
TRUE += name1.count("u") + name2.count("u") 
TRUE += name1.count("e") + name2.count("e") 
LOVE += name1.count("l") + name2.count("l") 
LOVE += name1.count("o") + name2.count("o") 
LOVE += name1.count("v") + name2.count("v") 
LOVE += name1.count("e") + name2.count("e") 
TRUE = str(TRUE)
LOVE = str(LOVE)
score = TRUE + LOVE
score = int(score)

if score < 10 or score > 90:
  answer += ", you go together like coke and mentos."
elif score > 40 and score < 50:
  answer += ", you are alright together."
else: 
  answer += "."
print(f"Your score is {score}" + answer)