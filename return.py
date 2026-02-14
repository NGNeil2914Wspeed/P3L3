def getint(question, min, max):
    while True:
        try:
            a = int(input(question))
            if (a > min and min is not None):
                break
            elif (a > max and max is not None):
                pass
            else:
                return a
        except ValueError as e:
            print (f"{e}\nplease enter a whole number")
            continue

name = input("Hey, could you enter your name? ")

print (f"Hey {name}, I'm gonna help you add some numbers so could you enter them below?")

num1 = getint("Enter the first number: ")
num2 = getint("Enter the second number: ")
print (num1+num2)