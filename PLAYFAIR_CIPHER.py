import string

class PlayfairCipher:
    def __init__(self, key,plaintext):
        self.key = key
        print('Key is : ',self.key)
        
        # prepare the key matrix
        alphabet = string.ascii_lowercase.replace('j','.') 
        print(alphabet)
        key_matrix = ['' for i in range(5)]
        
        i = 0
        j = 0
        
        for c in key:
            if c in alphabet:
                key_matrix[i] += c
                alphabet = alphabet.replace(c,'.')
                j +=1
                if j>4:
                    i+=1
                    j=0
                    
        for c in alphabet:
            if c !='.':
                key_matrix[i]+=c
                j+=1
                if j>4:
                    i+=1
                    j=0
        
        print(key_matrix)
                    
        # prepare pairs in plain text
        
        # prepare the key matrix
        self.plaintext = plaintext
        print(plaintext)

        plaintext_pairs = []
        ciphertext_pairs = []
        
        i=0
        while i < len(plaintext):
            first_letter = plaintext[i]
            second_letter = ''
            if(i + 1)== len(plaintext):
                second_letter = 'x'
            else:
                second_letter = plaintext[i+1]
            
            if first_letter != second_letter:
                plaintext_pairs.append(first_letter + second_letter)
                i+=2
            else:
                plaintext_pairs.append(first_letter + 'x')
                i+=1
        print(plaintext_pairs)
        
        
        

    # def encrypt(self, plaintext):
    #     encrypted_text = plaintext
    #     return encrypted_text
    
    # def decrypt(self, ciphertext):
    #     decrypted_text = ciphertext
    #     return decrypted_text

def main():
    while True:
        print("====================================================================")
        key = input("Enter the key: ")                      # Take user input for the shift value
        plaintext = input("Enter the text to encrypt: ")    # Take user input for the text to encrypt
        cipher = PlayfairCipher(key,plaintext)                        # Create an instance of the CaesarCipher class with the given shift

        # choice = input("Enter 'E' to encrypt or 'D' to decrypt: ")  # Ask if the user wants to encrypt or decrypt

        # if choice == 'E':                                   # If user chooses encryption
        #     plaintext = input("Enter the text to encrypt: ")# Take user input for the text to encrypt
        #     encrypted_text = cipher.encrypt(plaintext)      # Encrypt the input text using the created cipher
        #     print("Encrypted:", encrypted_text)             # Display the encrypted text
            
        # elif choice == 'D':                                 # If user chooses decryption
        #     ciphertext = input("Enter the text to decrypt: ") # Take user input for the text to decrypt
        #     decrypted_text = cipher.decrypt(ciphertext)     # Decrypt the input text using the created cipher
        #     print("Decrypted:", decrypted_text)             # Display the decrypted text
            
        # else:
        #     print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")  # Handle invalid input
            
if __name__ == "__main__":
    main()                                                  # Call the main function when the script is executed