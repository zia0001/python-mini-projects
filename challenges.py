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

