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
            print (f"{e}\nPlease enter a whole number")
            continue

name = input("Hey, could you enter your name? ")

print (f"Hey {name}, I'm gonna help you divide some numbers so could you enter them below?")

num1 = getint("Enter the first number: ", None, None)
num2 = getint("Enter the second number: ", None, None)
try:
    print (num1+num2)
except ZeroDivisionError:
    print ("These numbers cant be divided because one of the numbers is 0")