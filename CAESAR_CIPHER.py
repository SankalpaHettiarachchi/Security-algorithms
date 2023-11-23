class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift % 26  # Ensure the shift value is between 0 and 25

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            if char.isalpha():  # Check if the character is an alphabet
                shifted = ord(char) + self.shift  # Shift the character by the specified value
                if char.islower():  # Check if it's a lowercase letter
                    if shifted > ord('z'):  # Wrap around if shifted beyond 'z'
                        shifted -= 26
                elif char.isupper():  # Check if it's an uppercase letter
                    if shifted > ord('Z'):  # Wrap around if shifted beyond 'Z'
                        shifted -= 26
                encrypted_text += chr(shifted)  # Append the shifted character
            else:
                encrypted_text += char  # For non-alphabetic characters, keep as is
        return encrypted_text  # Return the encrypted text

    def decrypt(self, ciphertext):
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():  # Check if the character is an alphabet
                shifted = ord(char) - self.shift  # Reverse the shift by the specified value
                if char.islower():  # Check if it's a lowercase letter
                    if shifted < ord('a'):  # Wrap around if shifted before 'a'
                        shifted += 26
                elif char.isupper():  # Check if it's an uppercase letter
                    if shifted < ord('A'):  # Wrap around if shifted before 'A'
                        shifted += 26
                decrypted_text += chr(shifted)  # Append the shifted character
            else:
                decrypted_text += char  # For non-alphabetic characters, keep as is
        return decrypted_text  # Return the decrypted text


def main():
    while True:
        print("====================================================================")
        shift = int(input("Enter the shift key): "))  # Take user input for the shift value
        cipher = CaesarCipher(shift)  # Create an instance of the CaesarCipher class with the given shift

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


# ================================MyTry=============================================

# import string

# #
# plain_text = input("Enter message: ")
# key = int(input("Input the Key: "))
# shift = 3
# encrypted =[]

# for letter in plain_text:
    
#     if letter.isalpha():  
#         next_letter = chr(((ord(letter) - 97 + key) % 26) + 97) if letter.islower() else chr(((ord(letter) - 65 + key) % 26) + 65)
#         encrypted.append(next_letter)
#     else:
#         encrypted.append(letter)

# encrypted_msg = ''.join(encrypted)

# print('--------------------------------')
# print('Encrepted message',encrypted_msg)

# decrypted =[]
# for letter in encrypted_msg:
#     if letter.isalpha():
#         prev_letter = chr(((ord(letter) - 97 - key) % 26) + 97) if letter.islower() else chr(((ord(letter) - 65 - key) % 26) + 65)
#         decrypted.append(prev_letter)
#     else:
#         decrypted.append(letter)
        
# decrypted_msg = ''.join(decrypted)
# print('--------------------------------')
# print('Decrepted message',decrypted_msg)

