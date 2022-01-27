num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter Second number: "))
op = input("Enter operator(+, -, *, /): ")

if op == "+":
    print(f"Addition is:{num_1+num_2}")
elif op == "-":
    print(f"Subtraction is:{num_1-num_2}")
elif op == "*":
    print(f"Multiplication is:{num_1*num_2}")
elif op == "/":
    print(f"Division is: {num_1+num_2}")
else:
    print("Invalid operator")
