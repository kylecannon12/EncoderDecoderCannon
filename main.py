# antonio de guzman
from decode import decode
from encode import encode

encoded = ""
decoded = ""
while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")
    option = int(input("Please enter an option: "))

    if option == 1:
        password = int(input("Please enter your password to encode: "))
        encoded = encode(password)
        print("Your password has been encoded and stored!")
    elif option == 2:
        print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}")
    elif option == 3:
        break