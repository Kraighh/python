def add_numbers(a,b):
    print(a+b)

def add_numbers_type(a:int,b:int)->int:
    print(a+b)

add_numbers_type(1,2)

answer = 42
pi = 3.14159
print(answer+pi)
add_numbers(answer,pi)
add_numbers_type(answer,pi)

int(pi) == 3
float(answer) == 42.0

name = "PythonBo"
machine = "HAL"

print("Nice ti meet you {0}. I am {1}".format(name,machine))
print(f"Nice to meet you {name}. I am {machine}")

python_course = True
java_course = False
aliens_found = None

#if statments
number = 5
if number == 5:
    print("Number is 5")
else:
    print("Number is NOT 5")

if number:
    print("Number is defined and truthy")

text = "Python"
if text:
    print("Text is defined and truthy")

number = 3
python_course = True
if number == 3 and python_course:
    print("This will execute")

if number == 17 or python_course:
    print("This will also execute")

#ternary
a = 1
b = 2
print("bigger") if a > b else print("smaller")

#Lists
student_names = []
student_names = ["Mark", "Katarina", "Jessica"]
print(student_names)
print(student_names[0])
print(student_names[2])
print(student_names[-1])
student_names[0]="James"
print(student_names)
student_names.append("Homer")
student_names[0]="Mark"
print(student_names)
print("Mark" in student_names)
print(len(student_names))
del student_names[2]
print(student_names)
print(student_names[1:])
print(student_names[1:-1])