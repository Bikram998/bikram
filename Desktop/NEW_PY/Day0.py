'''CReating a list of cities in Nepal and Converting them to sets and tuples'''
Name = ("Kathmandu","Butwal","Neplgunj","Dhangadi","Mahendranagar","Bhairahwa")

print("Name OF Places", Name)
print(type(Name))

#Converting a string into integer type

Number = "9840806237";
print(Number)
print(type(Number))
print("")

print(int(Number))

'''Operations with complex number'''

cmp_number = 56+35j

cmp_1 = cmp_number.real
cmp_2 = cmp_number.imag

New_number = complex(67,12)
add = cmp_number + New_number
print(cmp_1)
print(cmp_2)
print(New_number)
print(add)
print("")


#dict:- all items are stored into key:value pair 

Var_items = {"mobile": "Keyboard", "Desktop": "Mouse", "Iphone":"Apple"}
print(Var_items)
print(type(Var_items))

Var_item = {"mobile": 2, "Desktop": 3, "Iphone":1}
print(Var_item)
print(type(Var_item))

a = 3**3
print("A=", a)
b = 5
print("A/B =", a//b)

# Conditional statement
#1. if statement syntax
#  if conditionn:
#     expression
a =0
if a == 0:
    print("NOOOOO")

# if else statements

if a== 0:
    print("OH MY GOD")
else:
    print("HAWA")

name = "Kathmandu"
if name == "kathmandu":
    print("1. Correct")

if name != "Villa":
    print("2. Correct")

if name == "Kathmandu" and name != "Kath":
    print("3. Correct")

# 2. if else statement
# to execute alternative expression if the condition
# is false

# syntax
# if condition:
#   expression
# else:
#   expression

light = "red"
if light == "red":
    print("Stop")
else:
    print("Steady and Go")

if light == "green":
    print("Go")
else:
    print("Stop")
    print("")

# if elif statement



day = input("Enter the day: ")
if day == "Sunday":
    print("First Day")
elif  day == "Monday":
    print("Second Day")
elif day == "Tuesday":
    print("Third Day")
elif day == "Wednesdy":
    print("Fourth Day")
elif day == "Thrusday":
    print("Fifth Day")
elif day == "Friday":
    print("Sixth Day")
elif day == "Saturday":
    print("Seventh Day")
else:
    print("No days")


# Nested if
# syntax
#  if conditions:
#     if conditions:
#        expression
#     else:
#          if conditions:
#             expression



code = 15
name = "Bikram"

input_code = int(input("Enter The Given Code! Please!: "))
if input_code == 15:
    input_name = input("Enter The Name: ")
    if input_name == "Bikram":
        print("Welcome")
    else:
        print("Invalid Name")
else:
    print("Invalid Code")
    

# Login sample for mobile OS

name = "Bikram"
Password = 9840806237

input_name = input("Please Enter Your Name: ")
if input_name == "Bikram":
    print("Welcome Bikram! Please Proceed Further!")
    input_Password = int(input("Please Input Your Password: "))
    if input_Password == 9840806237:
        print("Congratulation Bikram! Welcome To Successful Login!")
    else:
        print("Please Try Again")
else:
    print("Please Retry Your Name Again!")

#Tasks

Total_Fee = 500

input_Age = int(input("Please Provide your Age: "))
if input_Age < 10:
    print("Congratulation You Got Free Ride")
    if input_Age >= 10 and input_Age <=30:
        print("Have To Pay Full Fee!")
    elif input_Age >30:
        print("Congrates You Also Get Free Rides!")
    input_height = int(input("Please Enter Your HEight: "))
    if input_height < 5:
        print("You Got Free Ride")
    else:
        print("You Have to pay Full Fee!")
    input_card = input("Please Provide Your Card: ")
    if input_card == "Student Card":
        print("Congrates You Have Got 50% discount!")
    elif input_card == "Disabled Card":
        print("You have got 25% discount")
else:
    print("please Follow Instructions!")


