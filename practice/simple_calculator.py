first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

def calculate(first_num, second_num, operation):
    if operation == "+":
        result = sum(first_num, second_num)
    elif operation == "-":
        result = first_num - second_num
    elif operation == "*":
        result = first_num * second_num
    else:
        result = first_num / second_num
    message = print(f"The result is: {result}")
    return message

calculate(first_num, second_num, operation)


