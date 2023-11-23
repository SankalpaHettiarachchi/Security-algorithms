class PlayfairCipher:
    def __init__(self, key):
        self.key = key
        print('Key is : ',key)

    def encrypt(self, plaintext):
        encrypted_text = plaintext
        return encrypted_text
    
    def decrypt(self, ciphertext):
        decrypted_text = ciphertext
        return decrypted_text

def main():
    while True:
        print("====================================================================")
        key = input("Enter the key: ")  # Take user input for the shift value
        cipher = PlayfairCipher(key)  # Create an instance of the CaesarCipher class with the given shift

        choice = input("Enter 'E' to encrypt or 'D' to decrypt: ")  # Ask if the user wants to encrypt or decrypt

        if choice == 'E':  # If user chooses encryption
            plaintext = input("Enter the text to encrypt: ")  # Take user input for the text to encrypt
            encrypted_text = cipher.encrypt(plaintext)  # Encrypt the input text using the created cipher
            print("Encrypted:", encrypted_text)  # Display the encrypted text
        elif choice == 'D':  # If user chooses decryption
            ciphertext = input("Enter the text to decrypt: ")  # Take user input for the text to decrypt
            decrypted_text = cipher.decrypt(ciphertext)  # Decrypt the input text using the created cipher
            print("Decrypted:", decrypted_text)  # Display the decrypted text
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")  # Handle invalid input
            
if __name__ == "__main__":
    main()  # Call the main function when the script is executed