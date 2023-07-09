# read a file:- using r for read
# r is not necessary to read only opening is enough 

# # one way of storing data inside the file
# with open("names.txt","r") as file:
#     lines=file.readlines()

# another way to store data from file inside list is
names=[]
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
# print(names)
for line in sorted(names,reverse=True):
    # print(f"Hello, {name.rstrip()}")
    print(f"Hello, {line}")