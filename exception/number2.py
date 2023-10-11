def intput(prompt):
    while True:
        try:
            # if input is not int x will not be defined
            return int(input(prompt))
        except ValueError:
            # this block will run only when error is ValueError()

            # while catching errors you must know what the error is, it is a good practice

            # pass is used when we dont want to do anything when exception occurs
            pass

def main():
    y=intput("what is y? ")
    print(f"y is {y}")

main()
