def welcome():
    print("""
    ----------------------------------------------
                WELCOME TO ENCRYPTION GAME
    ----------------------------------------------
    This app allows you to encrypt and decrypt messages
    using various popular encryption methods. Whether
    you're learning encryption or experimenting with secure
    messages, this tool will help you understand how it works.
    ----------------------------------------------
    How it works:
    1. Select "Encrypt" or "Decrypt" from the menu
    2. Enter your message
    3. Choose an encryption/decryption method
    4. View the result and try different approaches
    ----------------------------------------------
    Press Enter to continue...
    """)
    input()

def main_menu():
    print("""
    ----------------------------------------------
                      MAIN MENU
    ----------------------------------------------
    1. Encrypt a message
    2. Decrypt a message
    3. View instructions
    4. Exit
    ----------------------------------------------
    """)
    choice = input("Please select an option: ")
    return choice

def instructions():
    print("""
    ----------------------------------------------
                      INSTRUCTIONS
    ----------------------------------------------
        **Caesar Cipher**
    The Caesar Cipher is a simple encryption technique where each letter in the message 
    is shifted by a specified number of positions in the alphabet.
    
    For example, if the shift (key) is 3:
      - A becomes D
      - B becomes E
      - C becomes F

       **Vigenère Cipher**
    The Vigenère Cipher is a more complex encryption method that uses a keyword to shift letters. 
    Instead of a single shift for the entire message, each letter in the message is shifted based 
    on the corresponding letter in the keyword.
    
    For example, with the keyword "KEY":
      - The first letter of the message is shifted by the position of 'K', the second by 'E', 
        and the third by 'Y'.
      - This pattern repeats for longer messages, cycling through the keyword.


    **How the Application Works**
    This application allows you to encrypt and decrypt messages using the Caesar and Vigenère ciphers.
    Follow these steps to use the app:
      1. Choose an option from the main menu:
         - Encrypt a message
         - Decrypt a message
         - View instructions
         - Exit the application
      2. For encryption or decryption:
         - Select your preferred cipher method (Caesar or Vigenère).
         - Enter the
          message you want to encrypt or decrypt.
         - Provide the required key (shift for Caesar or keyword for Vigenère).
      3. After encryption or decryption:
         - You can view the result.
         - Choose additional options to compare results, edit the message, or return to the main menu.

    ----------------------------------------------

    Press Enter to return to the main menu...
    """)
    input()

def encryption_menu():
    print("""
    ----------------------------------------------
                  ENCRYPTION OPTIONS
    ----------------------------------------------
    1. Caesar Cipher
    2. Vigenère Cipher
    3. Return to main menu




          **Caesar Cipher**
    The Caesar Cipher is a simple encryption technique where each letter in the message 
    is shifted by a specified number of positions in the alphabet.
    
    For example, if the shift (key) is 3:
      - A becomes D
      - B becomes E
      - C becomes F

       **Vigenère Cipher**
    The Vigenère Cipher is a more complex encryption method that uses a keyword to shift letters. 
    Instead of a single shift for the entire message, each letter in the message is shifted based 
    on the corresponding letter in the keyword.
    
    For example, with the keyword "KEY":
      - The first letter of the message is shifted by the position of 'K', the second by 'E', 
        and the third by 'Y'.
      - This pattern repeats for longer messages, cycling through the keyword.
    ----------------------------------------------
    """)
    choice = input("Please select an encryption method: ")
    return choice


def decryption_menu():
    print("""
    ----------------------------------------------
                  DECRYPTION OPTIONS
    ----------------------------------------------
    1. Caesar Cipher
    2. Vigenère Cipher
    3. Return to main menu






          **Caesar Cipher**
    The Caesar Cipher is a simple encryption technique where each letter in the message 
    is shifted by a specified number of positions in the alphabet.
    
    For example, if the shift (key) is 3:
      - A becomes D
      - B becomes E
      - C becomes F

       **Vigenère Cipher**
    The Vigenère Cipher is a more complex encryption method that uses a keyword to shift letters. 
    Instead of a single shift for the entire message, each letter in the message is shifted based 
    on the corresponding letter in the keyword.
    
    For example, with the keyword "KEY":
      - The first letter of the message is shifted by the position of 'K', the second by 'E', 
        and the third by 'Y'.
      - This pattern repeats for longer messages, cycling through the keyword.
    ----------------------------------------------
    """)
    choice = input("Please select a decryption method: ")
    return choice

def get_message():
    print("""
    ----------------------------------------------
                    ENTER MESSAGE
    ----------------------------------------------
    """)
    message = input("Please enter the message: ")
    return message

def get_key_caesar():
        print("""
    ----------------------------------------------
                    ENTER KEY
    ----------------------------------------------
    """)
        caesar_key = input("Please enter a key, an integer from 1-25: ")
        try:
            caesar_key = int(caesar_key)
            if 1 <= caesar_key <= 25:
                return caesar_key  # Valid key, exit the loop
            else:
                print("Error: The key must be an integer between 1 and 25.")
        except ValueError:
            print("Error: Please enter a valid integer.")
def get_key_vigenere():
        print("""
    ----------------------------------------------
                    ENTER KEY
    ----------------------------------------------
    """)
        vigenere_key = input("Please enter a key, a word or characters with at least 2 alphabetic characters: ")
        if vigenere_key.isalpha() and len(vigenere_key) >= 2:
            return vigenere_key  
        else:
            print("Error: The key must be at least 2 alphabetic characters long.")



#Logic of this algorithm is taken from https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
def caesar_encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_message += chr((ord(char) - 97 + key) % 26 + 97)
            else:
                encrypted_message += chr((ord(char) - 65 + key) % 26 + 65)
    return encrypted_message

def caesar_decrypt(message, key):
    return caesar_encrypt(message, -key)

#Logic of this algorithm is taken from https://www.geeksforgeeks.org/vigenere-cipher/
def vigenere_encrypt(message, key):
    encrypted_message = ""
    key_index = 0
    for char in message:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - 97
            if char.islower():
                encrypted_message += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_message += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            encrypted_message += char
    return encrypted_message

    
#Logic of this algorithm is taken from https://www.geeksforgeeks.org/vigenere-cipher/
def vigenere_decrypt(message, key):
    decrypted_message = ""
    key_index = 0
    for char in message:
        if char.isalpha():
            shift = 26 - (ord(key[key_index % len(key)].lower()) - 97)
            if char.islower():
                decrypted_message += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                decrypted_message += chr((ord(char) - 65 + shift) % 26 + 65)
            key_index += 1
        else:
            decrypted_message += char
    return decrypted_message

def encryption_loop():
    choice = encryption_menu()
    
    while True:
        if choice == '1':
            message = get_message()
            encryption = 'Caesar Cipher'
            key = get_key_caesar()
            result = caesar_encrypt(message, key)
        elif choice == '2':
            message = get_message()
            encryption = 'Vigenère Cipher'
            key = get_key_vigenere()
            result = vigenere_encrypt(message, key)
        elif choice == '3':
            return
        else: 
            print('invalid input returning to main menu')
            return
        while True:
            choice = results_menu_encryption(result,key,encryption)
            if choice == '1':
                comparision(message, key,encryption)
            elif choice == '2':
                message= edit_message(message)
                if encryption == 'Caesar Cipher':
                    result = caesar_encrypt(message, key)
                elif encryption == 'Vigenère Cipher':
                    result = vigenere_encrypt(message, key)
            elif choice == '3':
                return


def decryption_loop():
    choice = decryption_menu()  
    
    while True:
        if choice == '1':
            message = get_message()
            encryption = 'Caesar Cipher'
            key = get_key_caesar()
            result = caesar_decrypt(message, key)
        elif choice == '2':
            message = get_message()
            encryption = 'Vigenère Cipher'
            key = get_key_vigenere()
            result = vigenere_decrypt(message, key)
        elif choice == '3':
            return  
        else: 
            print('Invalid input. Returning to main menu.')
            return
        
        # Decryption result loop
        while True:
            choice = results_menu_decryption(result, key, encryption)
            if choice == '1':  
                message = edit_message(message)
                
                if encryption == 'Caesar Cipher':
                    result = caesar_decrypt(message, key)
                elif encryption == 'Vigenère Cipher':
                    result = vigenere_decrypt(message, key)
            elif choice == '2':  
                return
            else:
                print("Invalid option. Please try again.")





def comparision(message,key,type):
    if type == 'Caesar Cipher':
        result = caesar_encrypt(message, key)
        new_key = get_key_vigenere()
        other_result = vigenere_encrypt(message, new_key)
        other_encryption_type = 'Vigenère Cipher'
    else:
        result = vigenere_encrypt(message, key)
        new_key = get_key_caesar()
        other_result = caesar_encrypt(message, new_key)
        other_encryption_type = 'Caesar Cipher'
    
    print(f"""
    ----------------------------------------------
                  Comparison Results
    ----------------------------------------------
    1. {type}: {message} -> {key}: {result}
    2. {other_encryption_type}: {message} -> {new_key}: {other_result}
    ----------------------------------------------
    """)


def results_menu_encryption(results, key,type):
        print(f"""
    ----------------------------------------------
                      Results
    ----------------------------------------------
    Result: {type} key = {key}: {results}
    ----------------------------------------------
                      OPTIONS
    ----------------------------------------------
    1. Compare results with other encryption methods
    2. Edit the message or enter new message
    3. Return to main menu (Warning: Message will be lost forever)
    ----------------------------------------------
    """)
        choice = input("Please select an option: ")
        return choice


def results_menu_decryption(results, key, encryption_type):
    print(f"""
    ----------------------------------------------
                      Results
    ----------------------------------------------
    Decrypted Result: {encryption_type} (key = {key}): {results}
    ----------------------------------------------
                      OPTIONS
    ----------------------------------------------
    1. Edit the message or enter new message
    2. Return to main menu (Warning: Message will be lost forever)
    ----------------------------------------------
    """)
    choice = input("Please select an option: ")
    return choice


def edit_message(current_message):
    print(f"Current message: {current_message}")
    new_message = input("Press Enter to keep the current message or enter a new message: ")
    if new_message.strip() == "":  
        return current_message
    return new_message



def main():
    welcome()


    while True:
        choice = main_menu()
        
        if choice == '1':  # Encrypt a message
            encryption_loop()
        elif choice == '2':  # Decrypt a message
            decryption_loop()
        elif choice == '3':  # View Instructions
            instructions()
        elif choice == '4':  # Exit
            print("""
    ----------------------------------------------
            Are you sure you want to exit
    ----------------------------------------------
    1. Yes I want to exit
    2. No return to main menu
    ----------------------------------------------
            """)
            exit_choice = input("Please enter your choice: ")
            if exit_choice == '1':
                print("Exiting the game. Goodbye!")
                break
            else:
                print("returning to main menu")
                continue
        else:
            print("Invalid option. Please try again.")


main()