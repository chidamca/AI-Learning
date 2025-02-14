#1.	Print a greeting message saying “Welcome to Python – It is a great language!!! “
print("Welcome to Python – It is a great language!!! ")

#2.	Define a variable and display the type of that variable
name = "chida"
print(type(name))

#3.	Write a program that asks the user for a first name and then asks the user for a last name. The program should print the first and last names together on the same line
firstName = input("Enter the first name : ")
lastName = input("Enter the lastName name : ")

print("Full Name is : ", firstName , lastName)

#4.	Write a program that prompts for a string and a number and prints out the string the number of times indicated by the number
str = input("Enter a string: ")
number = int(input("Enter a number: "))

print((str + "\n") * number)

#5.	Enter an email address from the user and check if the address is valid (hint – check for the presence of @ sign)# Ask the user for an email address
email = input("Enter an email address: ")

if '@' in email and email.count('@') == 1:
    print("The email address is valid.")
else:
    print("The email address is invalid.")


#6.	Input your age into a variable called age. Have the computer printout how old you'll be eight years from now, ten years from now, twenty-four years from now. 
age = int(input("Enter your age: "))


age_in_8_years = age + 8
age_in_10_years = age + 10
age_in_24_years = age + 24

print(f"In 8 years, you will be {age_in_8_years} years old.")
print(f"In 10 years, you will be {age_in_10_years} years old.")
print(f"In 24 years, you will be {age_in_24_years} years old.")

#7.	Write a program that asks a user for five flowers, and then store them in a list called flowerlist and print them out in alphabetical order. 

flowerlist = []
for i in range(5):
    flower = input(f"Enter flower {i + 1}: ")
    flowerlist.append(flower)

flowerlist.sort()

print("Flowers in alphabetical order:")
for flower in flowerlist:
    print(flower)

# 8.You are a shopkeeper who sells fruits. All the fruits that you sell have been stored in a dictionary as name vs price. You read through the dictionary and let your customers know about the details
fruits = {
    "Apple": 1.50,
    "Banana": 0.50,
    "Orange": 1.00,
    "Mango": 2.50,
    "Grapes": 2.00,
    "Pineapple": 3.00,
    "Watermelon": 5.00
}

print("Welcome to our fruit shop! Here are the fruits we sell:")
for fruit, price in fruits.items():
    print(f"- {fruit}: ${price:.2f}")

choice = input("\nWould you like to buy any fruit? (yes/no): ").strip().lower()
if choice == "yes":
    fruit_name = input("Enter the name of the fruit you want to buy: ").strip().title()
    if fruit_name in fruits:
        quantity = int(input(f"How many {fruit_name}s would you like to buy? "))
        total_cost = fruits[fruit_name] * quantity
        print(f"That will cost you ${total_cost:.2f}.")
    else:
        print("Sorry, we don't have that fruit in our shop.")
else:
    print("Thank you for visiting our shop. Have a great day!")

# 9. Ask the user to input a number between 1 to 10.Give the user 3 chances to enter the number correctly. If the user enters correctly then print the number entered by the user. Else quit with an error message saying “Sorry, your chances are over!!!”

chances = 3

for attempt in range(chances):
    number = int(input(f"Attempt {attempt + 1}: Enter a number between 1 and 10: "))
   
    if 1 <= number <= 10:
        print(f"You entered the correct number: {number}")
        break
    else:
        print("Invalid number. Please try again.")

else:
    print("Sorry, your chances are over!!!")

# 10. Write a program to print first 50 prime numbers
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Initialize variables
prime_count = 0
number = 2
prime_numbers = []

# Find and store the first 50 prime numbers
while prime_count < 50:
    if is_prime(number):
        prime_numbers.append(number)
        prime_count += 1
    number += 1

# Print the first 50 prime numbers
print("The first 50 prime numbers are:")
print(prime_numbers) 