# ------------------------------------------------------------------

"""
patient_name = "John Smith"
age= 50
is_new = True

"""
# ------------------------------------------------------------------
"""
# name = input('what is your name? ')
# favourite_color = input('what is your favourite color ')
# print(name + ' likes ' + favourite_color)
"""
# ------------------------------------------------------------------
# convert user weight in pounds to kgs
"""
weight_lbs = (input('what is yout weight in pounds: '))
weight_kgs = round(int(weight_lbs) * 0.453592,2)
print('your weight in kgs = ' +str(weight_kgs) + ' kgs' )

                    # OR
try:

    weight = int(input('what is yout weight in pounds: '))
    weight_kgs = round(weight * 0.453592, 2)

    print(f'your weight is {weight_kgs} kgs')

except ValueError:
    print('please enter a valid number for weight')

    """
# -------------------------------------------------------------------
'''
x = (2+3) * 10 - 3
print(x)

'''
# ------------------------------------------------------------------
'''
house_price = 1000000
buyer_credit = 1100000

if buyer_credit >= house_price:
    down_payment = house_price * 0.1
    print(f'Down payment is ${down_payment} ' )
else:
    down_payment = house_price *0.2
    print(f'down payment is ${down_payment}')

    '''
# --------------------------------------------------
'''
name = 'Thomas Edison'

if len(name) < 3:
  print('name must be at least 3 characters')
elif len(name) > 50:
  print('name must be less than 50 characters')
else:
  print('name looks good')

  '''
# --------------------------------------------------
'''
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == 'L':
  converted = round(weight * 0.45359237, 2)
  print(f"You are {converted} kilos")
else:
  converted = round(weight/0.45359237, 2)
  print(f"You are {converted} lbs")
  '''
# --------------------------------------------------

'''
secret_number = 7
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
  guess = int(input("Guess: "))
  guess_count +=1
  if guess == secret_number:
    print("You Won")
    break
else:
    print("You Lost")

    '''
# --------------------------------------------------
'''
command = ""
started = False
while True:
   command = input("< ")
   if command.lower() == "help":
     print("""
    start - to start the car
    stop - to stop the car
    quit - to quit the game
    """)
   elif command.lower() == "start":
      if started:
        print("Car already Started!")
      else:
        started = True
        print("Car started")
   elif command.lower() == "stop":
      if not started:
         print("Car already stopped!")
      else:
         started = False
         print("Car stopped")

   elif command.alreadylower() == "quit":
       break
   else:
    print("Enter a correct command")

  '''
# ---------------------------------------------------


'''
prices = [10, 20, 30]


total = 0
for price in prices:
  total = total + price
print(f"Total = {total}")

'''
# ---------------------------------------------------

'''

numbers = [5, 2, 5, 2,2]

for number in numbers:
  print( "*" * number)

'''
''' OR Using inner loop'''
'''
numbers = [1, 1, 1, 1, 5]

for number in numbers:
    output = ""
    for count in range(number):
        output += 'x'
    print(output)
    '''
# ---------------------------------------------------
'''
            Finding maximum in List
numbers = [1,2,3,4,5,6,7,8,9]
largest = max(numbers)
print(largest)
'''
'''
OR USING LOOP
'''
'''
numbers = [111,23,34,445,546,65,733,9]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print(maximum)
'''
#------------------------------------------
'''      Finding minimum in list   '''

'''

numbers = [3,4,5,89,4,3,7,1,2]
min = numbers[0]

for number in numbers:
     if number < min:
         min = number
print(min)

'''
#--------------------------------------
'''           2D List   '''
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[2][1])
for row in matrix:
    for item in row:
        print(item)

'''
#--------------------------------------
'''           Removing Duplicate from  a list   '''

'''

numbers = [1,2,3,4,4,5,6,7,8,8,9,9]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)

'''
#--------------------------------------
'''      Tuple:   Similar to list but cannot be modified   '''

'''

secret_numbers = (323,555,5454)
# secret_numbers[0] = 776  can't be modified
print(secret_numbers)

'''

#--------------------------------------
'''Dictionaries:  just like objects in JS'''

'''
customer = {
    "name": "zia",
    "age":  24,
    "is_logged_in": False
}

print(customer["name"], customer["is_logged_in"])
print(customer.get("name"))

'''

#--------------------------------------
'''      Numbers to words OR Number mapper   '''

'''

number = input("Enter a number: ")
number_mapping = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
}
output = ""
for letter in number:
    output += number_mapping.get(letter, "!") + " "
print(output)
'''

#----------------------------------------------
'''         Text to emojis       '''

'''

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😄",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

'''

# ------------------------------------------------------------------
'''   Functions  '''

'''

def greet_customer(first_name, last_name):
    print(f'Hi {first_name} {last_name} welcome to our website')


greet_customer("Subhan", "Raheem")
greet_customer("Ali", "Amin")

'''
# ------------------------------------------------------------------
'''     Text to emoji using function   '''
'''

def text_to_emoji(message):
    words = message.split(' ')
    emojis = {
        ":)": "😄",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return(output)

text = input(">")
text_to_emoji(text)
print(text_to_emoji(text))
'''

# ------------------------------------------------------------------
'''Exception handling'''
'''

try:
    age = int(input('Age:'))
    print(age)
    salary = 234383
    risk = salary/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid value')

'''

# ------------------------------------------------------------------
'''    Classes  '''


'''

class Animals:
    def cat(self):
        print("Hi! I am cat from lions family")
    def dog(self):
        print("Hi! I am Dog and i like playing")



a = Animals()
a.dog()


cclass Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


p1 = Person("Jack")
p2 = Person("Ali")
Sarah = Person("Sarah")

print(p1.name)
print(p2.name)
p1.talk()
p2.talk()
Sarah.talk()

'''

#--------------------------------------------------------------
'''      Inheritance    '''

'''

class Birds:
    def fly(self):
        print("fly")

class Duck(Birds):
    def swim(self):
        print("swim")


class turkey(Birds):
    pass


duck1 = Duck()
duck1.fly()
duck1.swim()
'''
#-------------------------------------------------
'''        Modules          '''

'''
import converters
from converters import kg_to_lbs
from converters import lbs_to_kg

kg_to_lbs(67)
lbs_to_kg(166)

def lbs_to_kg(weight):
    weight_in_kg = weight * 0.453592
    print(weight_in_kg)
    return weight_in_kg



def kg_to_lbs(weight):
    weight_in_lbs = weight / 0.453592
    print(weight_in_lbs)
    return weight_in_lbs

'''

'''
def find_max_in_list(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            max = number
    print(maximum)
    
import number_tools
from number_tool import find_max_in_list
numbers = [34,87,54,8,43]
find_max_in_list(numbers)

'''

'''    Builtin radom module      Random member selection'''
'''
import random

members = ['hameed', 'salar','wasim']
selected_member = random.choice(members)
print(selected_member)

'''

'''Random dice rolling'''
'''
import random
from calendar import firstweekday


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        return (first, second)


dice = Dice()
dice.roll()
print(dice.roll())
'''
#----------------------------------------------------------------
'''    Packages   '''

'''
def cal_shipping():
    print('shipping cost')

from ecommerce.shipping import cal_shipping
cal_shipping()
'''

#-------------------------------------------------------------------
'''Files and Directories using pathlib'''

'''
from pathlib import Path

path = Path()
for file in path.glob('*.py'):
    print(file)
'''

'''
from pathlib import Path

path = Path("emails")
print(path.mkdir())

'''

'''
from pathlib import Path

path = Path("emails")
print(path.rmdir())
'''

'''

from pathlib import Path

path = Path("number_tools.py")
print(path.exists())

'''
