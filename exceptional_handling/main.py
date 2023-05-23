try:
    print(54 / 0)
except NameError:
    print("An exception occurred")
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print("successfully completed without any error")

finally:
    print("finally is executed")
