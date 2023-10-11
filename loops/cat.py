# for i in ["I","Am","Cat"]:
#     print("Meow")
# for i in range(3):
#     print("Meow")

# print("Meow\n"*3)
# print("Meow\n"*3, end="")

# while True:
#     n=int(input("What is n? "))
#     if n>0:
#         break
# for i in range(n):
#     print("Meow")

def main():
    number=get_num()
    meow(number)
def get_num():
    while True:
        n=int(input("Give n: "))
        if n>0:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()