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

total = getint(100, 1, None)
paid = getint(100, 1, total)
if total == paid:
    print ("Amount paid")
else:
    print (f"Pay {total-paid} more")