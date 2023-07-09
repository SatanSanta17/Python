
# with open("students.csv") as file:
#     for line in file:
#         row=line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

# # assigning 2 variables at one time when we know that line returns 2 values
# with open("students.csv") as file:
#     for line in file:
#         name,house=line.rstrip().split(",")
#         print(f"{name} is in {house}")
        
# creating a list of dictionary students where i want to store both name and house
students=[]
with open("students.csv") as file:
    for line in file:
        # creating two variables name and house which store 2 values that are returned by file
        name,house=line.rstrip().split(",")
        # creating a dictionary called student where "name" and "house" is stored
        student={"name":name,"house":house}
        students.append(student)

# a function that returns the name of a student
def get_name(student):
    return student["name"]

# sorts a list of dictionary by using he key name
for student in sorted(students,key=get_name):
    print(f"{student['name']} is in {student['house']}")