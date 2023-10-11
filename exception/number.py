def intput():
    while True:
        try:
            # if input is not int x will not be defined
            x=int(input("What is x? "))
            # break
        except ValueError:
            # this block will run only when error is ValueError()
            # while catching errors you must know what the error is, it is a good practice
            print("x is not an integer\n", "please put an integer",sep="")
        else: 
            # if there are no errors only then this code will run
            return x

def main():
    x=intput()
    print(f"x is {x}")

main()
