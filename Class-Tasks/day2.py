'''student={'name':'Riya','age':21,'cgpa':8.5}
class_data=[{'name':'Riya','marks':85},
            {'name':'Arjun','marks':92},
            {'name':'Priya','marks':78}]
print (student.keys())
print(student.values())
print(student.items())
#Loop through keys
for key in student:
    print(key,'->',student[key])
#Loop through key-value pair (best way)
for key,value in student.items():
    print(f"{key}:{value}")
for s in class_data:
    print(f"{s['name']} Scored {s['marks']}")'''


'''student = []

def add_student(name, rollno, age):
    stu = {'Name': name, 'Rollno': rollno, 'Age': age}
    student.append(stu)

def display(student):
    for i in student:
        print(f"Name: {i['Name']}, Rollno: {i['Rollno']}, Age: {i['Age']}")

def search(student,name):
    for i in student:
        if i['Name'] == name:
            print(f"Name: {i['Name']}, Rollno: {i['Rollno']}, Age: {i['Age']}")
            return
    print("Student not found")

add_student('deepak',20,23)
add_student('ram',20,23)
display(student)
search(student,'deepak')'''
        
# challenge: Give marks =[45,82,67,91,38,75] find: Total, Average,Highest and How many Passed(>=35) make the funtion of all and the call then and also take the marks input fron user
'''marks=[45,82,67,91,38,75] 

def Total(marks):
    s=0
    for i in marks:
        s+=i
    return s

def Average(marks):
    return Total(marks)/len(marks)

def Heigh(marks):
    hei=0
    for i in marks:
        if (hei<i):
            hei=i
    return hei

def student(marks):
    count=0
    for i in marks:
        if (i>=35):
            count +=1
    return count

print(Total(marks))
print(Average(marks))
print(Heigh(marks))
print(student(marks))'''

'''num=lambda x,y: x+y
print(num(4,6))

student=[{'name':'Riya','marks':85},
            {'name':'Arjun','marks':92},
            {'name':'Priya','marks':78}]
student.sort(key=lambda s: s['marks'])
print(student)
student.sort(key=lambda x:x['name'])
print(student)
student.sort(key=lambda s: s['marks'],reverse=True)
print(student)
'''

marks= [10, 20, 35, 40, 50]

# Double each element
'''doubled = [num * 2 for num in numbers]

# Select values greater than 70
result = [num for num in doubled if num > 70]

print(result)'''

'''double=(map(lambda m:m *2,marks))
print(double)

passed=(filter(lambda m:m>=15,marks))
print(passed)'''

# List Comprehension 
'''
sqares=[m**2 for m in marks]
print(sqares)
passed=[m for m in marks if m>=20]
grades=['pass' if m>=15 else 'Fail' for m in marks]
'''

student = []

def add_student(name, roll_number, marks):
    if marks >= 80:
        grade = 'A'
    elif marks >= 60:
        grade = 'B'
    else:
        grade = 'C'

    student.append({
        'name': name,
        'roll_number': roll_number,
        'marks': marks,
        'grade': grade
    })

def show_all():
    for s in student:
        print(f"Name: {s['name']}, Roll No: {s['roll_number']}, Marks: {s['marks']}, Grade: {s['grade']}")

# Add students
add_student("Riya", 20, 85)
add_student("Arjun", 22, 92)
add_student("Priya", 19, 78)


# Display students
show_all()

# Statistics
total = 0
highest = 0
passed = 0

for s in student:
    total += s['marks']

    if s['marks'] > highest:
        highest = s['marks']

    if s['marks'] >= 40:
        passed += 1

average = total / len(student)
print("Students Passed:", passed)