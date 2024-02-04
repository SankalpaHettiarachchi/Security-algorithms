class CaesarCipher:
    def __init__(self, shift):
        # Ensure the shift value is between 0 and 25
        self.shift = shift % 26                     

    def encrypt(self, plaintext):
        encrypted_text = ""
        for char in plaintext:
            # Check if the character is an alphabet
            if char.isalpha():
                # Shift the character by the specified value                      
                shifted = ord(char) + self.shift    
                # Check if it's a lowercase letter
                if char.islower():  
                    # Wrap around if shifted beyond 'z'               
                    if shifted > ord('z'):          
                        shifted -= 26
                elif char.isupper():                
                    if shifted > ord('Z'):          
                        shifted -= 26
                # Append the shifted character
                encrypted_text += chr(shifted)  
            # For non-alphabetic characters, keep as is    
            else:
                encrypted_text += char              
        return encrypted_text                   

    def decrypt(self, ciphertext):
        decrypted_text = ""
        for char in ciphertext:
            # Check if the character is an alphabet
            if char.isalpha():   
                # Reverse the shift by the specified value                   
                shifted = ord(char) - self.shift  
                # Check if it's a lowercase letter  
                if char.islower(): 
                    # Wrap around if shifted before 'a'                 
                    if shifted < ord('a'):          
                        shifted += 26
                elif char.isupper():                
                    if shifted < ord('A'):          
                        shifted += 26
                decrypted_text += chr(shifted)      
            else:
                decrypted_text += char              
        return decrypted_text                      


def main():
    while True:
        print("====================================================================")
        shift = int(input("Enter the shift key): "))# Take user input for the shift value
        cipher = CaesarCipher(shift)                # Create an instance of the CaesarCipher class with the given shift

        choice = input("Enter 'E' to encrypt or 'D' to decrypt: ")  # Ask if the user wants to encrypt or decrypt

        if choice == 'E':                           # If user chooses encryption
            plaintext = input("Enter the text to encrypt: ")  # Take user input for the text to encrypt
            encrypted_text = cipher.encrypt(plaintext)  # Encrypt the input text using the created cipher
            print("Encrypted:", encrypted_text)     # Display the encrypted text
            
        elif choice == 'D':                         # If user chooses decryption
            ciphertext = input("Enter the text to decrypt: ")  # Take user input for the text to decrypt
            decrypted_text = cipher.decrypt(ciphertext)  # Decrypt the input text using the created cipher
            print("Decrypted:", decrypted_text)     # Display the decrypted text
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")  # Handle invalid input
            
if __name__ == "__main__":
    main()                                          # Call the main function when the script is executed



