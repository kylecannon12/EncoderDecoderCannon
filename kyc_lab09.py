def encoder(password):
    encoded = ""
    for i in str(password):
        new_digit = (int(i) + 3) % 10
        encoded += str(new_digit)
    return encoded


def main():
    if True:
        print("-------------")
        print("1. Encode\n2. Decode\n 3. Quit")
        option = int(input("Please enter an option: "))
        password = int(input("Please enter your password to decode: "))
        if option == 1:
            encoded = encoder(password)
            print("Your password has been encoded and stored!")

        if option == 2:

