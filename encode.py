#kyle cannon
def encode(password):
    encoded = ""
    for i in str(password):
        new_digit = (int(i) + 3) % 10
        encoded += str(new_digit)
    return encoded



