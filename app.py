def print_welcome():
    print("Welcome to the Alien Language Decoder!")
    print("Alien messages use unique symbols.")
    print("You will try to decode the message by mapping symbols to letters.\n")

def get_alien_message():
    # Alien symbols are represented by special characters
    print("Here is the alien message:")
    message = "@#*#& @&* #*!!"
    print(message)
    return message

def get_mapping():
    print("\nThe alien language uses these symbols:")
    print("@ # * & !")
    print("Map each symbol to an English letter (a-z).")
    mapping = {}
    symbols = ['@', '#', '*', '&', '!']
    
    for sym in symbols:
        while True:
            letter = input(f"Enter letter for symbol '{sym}': ").lower()
            if len(letter) == 1 and letter.isalpha():
                mapping[sym] = letter
                break
            else:
                print("Invalid input. Please enter a single letter.")
    return mapping

def decode_message(message, mapping):
    decoded = ""
    for char in message:
        if char in mapping:
            decoded += mapping[char]
        else:
            decoded += char
    return decoded

def main():
    print_welcome()
    message = get_alien_message()
    mapping = get_mapping()
    print("\nDecoding the message with your mappings...\n")
    decoded_message = decode_message(message, mapping)
    print("Decoded message:")
    print(decoded_message)
    print("\nThank you for using the Alien Language Decoder!")

if __name__ == "__main__":
    main()
