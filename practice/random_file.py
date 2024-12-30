import random
import string

def random_file():
    filename = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    with open(f"{filename}.txt", "w") as file:
        file.write(filename)
    message = print(f"File '{filename}.txt' has been created with the content: {filename}")
    return message


random_file()