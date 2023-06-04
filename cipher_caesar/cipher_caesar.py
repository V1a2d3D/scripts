alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypter(message, key):
    result = ''
    for symbol in message:
        if symbol in alphabet:
            symbol_index = alphabet.find(symbol)
            index = symbol_index+key
            if index < 0 or index < 25:
                result += alphabet[index]
            else:
                new_index = (index % 25) - 1
                result += alphabet[new_index]
        else:
            result += symbol
    return result


while True:
    line = input("\nEnter the message for encryption\n(Enter 'q' to exit): ").upper()
    if line == "Q":
        print("\nGoodbye!")
        break

    step = int(input("Enter the key for encryption: "))

    encryption_result = encrypter(line, step)
    print(f"\nResult: {encryption_result}")
