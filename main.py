#Sophie Ruetschi
def encoder(password):
    newPass = ""

    for char in password:
        res = 3 + int(char)
        newPass += str(res)

    return newPass


def decoder(password):
    """written by Derek Molina"""
    decoded_password_list = [int(chars) - 3 for chars in encoded]
    return ''.join(map(str, decoded_password_list))


if __name__ == '__main__':
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    selection = int(input("Please enter a menu option: "))
    password = ""
    encoded = ""

    while selection != 3:
        if selection == 1:
            password = input("Please enter your password to encode:")
            encoded = encoder(password)
            print("Your password has been encoded and stored!")
        elif selection == 2:
            print("The encoded password is ", encoded, ", and the original password is ", decoded(encoded), " .", sep="")

        print()
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        selection = int(input("Please enter a menu option: "))


