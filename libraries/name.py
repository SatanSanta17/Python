import sys

# # sys.argv is a list of arguments that we pass in command line
# print(f"Hello, my name is {sys.argv[1]}")
    
# # we can use exception handeling so the code doesnt break if no arguments is passed
# try:
#     print(f"Hello, my name is {sys.argv[1]}")
# except IndexError:
#     print("Too few arguments")

# # another way to save the code is
# if len(sys.argv)<2:
#     print("Too few arguments")
# else:
#     print(f"Hello, world my name is {sys.argv[1]}")

# # since it is not a good practice to run the actual required code in if or else block we'll use a different approach
# # we'll use sys.exit() which ends the program
# if len(sys.argv)<2:
#     sys.exit("Too few arguments")
# print(f"Hello, world my name is {sys.argv[1]}")

# to access the argv list
if len(sys.argv)<2:
    sys.exit("Too few arguments")
# # we are here slicing the list using '[start:end]' i haven't mentioned anything after ':' because i want to go till the end 
# for arg in sys.argv[1:]:
#     print(f"hello, my name is {arg}")

# we can also slice something from the end using negative numbers for example:
for arg in sys.argv[1:-2]:
    print(f"hello, my name is {arg}")