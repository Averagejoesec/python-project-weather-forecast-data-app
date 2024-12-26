num = float(input("Enter a number: "))

def pos_or_neg(number):
    if number >= 0:
        result = "positive"
    else:
        result = "negative"
    message = print(f"The number is {result}.")
    return message


pos_or_neg(num)