# Except Method for any error at all
try:
    x = int(input('Input an integer: '))
    print(x)

# If there is an error this is executed.
except ValueError:
    print('Value not valid')
# If there is no error this is executed

else:
    print('Nothing went wrong')

# Weather there is an error or not this gets executed at the end.
finally:
    print("Try Except finished")
