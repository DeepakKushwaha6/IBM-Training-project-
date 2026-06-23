'''name="deepak"
age="20"
dept="CSEAIML"
cgpa="6.91"
print('---student progile---')
print('name:',name)
print('age:',age)
print('dept:',dept)
print('cgpa:',cgpa)
print(type(cgpa))'''


'''age=input("enter your age:")
print(age + 10)'''

'''age=int(input("enter your age:"))
print('In 10 years:',age + 10)
print(type(age))

gpa=float(input("enter your cgpa:"))
print('your cgpa is:',gpa)
print(type(gpa))'''

'''a=int(input("enter a number:"))
b=int(input("enter another number:"))
print('sum:',a+b)
print('difference:',a-b)
print('product:',a*b)
print('Devide:',a/b)
print('Remainder:',a%b)'''

'''a=int(input("enter a number:"))
if a%2==0:
    print('even')
else:
    print('odd')'''


'''for i in range(1,11):
    print(i)'''

'''for i in range(0,11):
    print(i)'''

'''Marks=int(input("enter your marks:"))
if Marks>=90:
    print('Grade: A')
elif Marks>=80:
    print('Grade: B')
elif Marks>=70:
    print('Grade: C')
elif Marks>=60:
    print('Grade: D')   
else:    print('Grade: F')'''

'''name=input("enter your name:")
age=int(input("enter your age:"))
print(f'hello My Name is {name} and I am {age} years old.')'''

# FizzBuzz Classic Problem
'''i = int(input("Enter a number: "))
if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
elif i % 3 == 0:
        print("Fizz")
elif i % 5 == 0:
        print("Buzz")
else:
        print(i)'''

# sum of Digits
'''num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10
print("Sum of digits:", sum_of_digits)'''

# Palindrome Checker
'''num = int(input("Enter a number: "))
original_num = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
if original_num == reversed_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")'''

# Number Guessing Game
'''import random
number_to_guess = random.randint(1, 100)
attempts = 0
while True:
    user_guess = int(input("Guess the number (between 1 and 100): "))
    attempts += 1
    if user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break'''

'''marks = [85, 92, 78, 95, 60]
name=['Riya','Deepak','Rohit','Anjali','Sita']
for i in range(len(marks)):
    if marks[i] >= 90:
        print(f"{name[i]} has scored an A grade.")'''

n = int(input("Enter number of elements: "))

lst = []
for i in range(n):
    element = input(f"Enter element {i+1}: ")
    lst.append(element)

print(lst)

