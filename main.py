def encrypt():
    message = input("Please Enter your message: ")
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 5
    encrypt = ' '
    for i in message:
        position=alphabet.find(i)
        newposition=(position+5)%26
        encrypt+=alphabet[newposition]

    print(encrypt)

def decrypt():
    message = input("Please Enter your message: ")
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key = 5
    encrypt = ' '
    for i in message:
        position=alphabet.find(i)
        newposition=(position-5)%26
        encrypt+=alphabet[newposition]

    print(encrypt)


def main():
    option = input("Encryption(E)/Decyption(D):")
    if option == "E":
        encrypt()
    elif option == "D":
        decrypt()
    else:
        print("Please enter a valid choice.")
    
main()