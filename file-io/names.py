# we store the data that we need to use again and again in a file.
# we'll see how to access files using code

name=input("what's your name? ")

# #writing in a file:- we use a-append to add in file coz w-write overrides entirely whenever we run this code
# file=open("names.txt","a")
# file.write(f"{name}\n")
# file.close()

# with keyword:
with open("names.txt","a") as file:
    file.write(f"{name}\n")

