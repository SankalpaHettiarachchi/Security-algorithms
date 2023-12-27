import string

class PlayfairCipher_Encryption:
    def __init__(self, key,plaintext):
        self.key = key
        print('Key is : ',self.key)
        print('Plaintext is : ',plaintext)
        
        # prepare the key matrix
        alphabet = string.ascii_lowercase.replace('j','.') 
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
                            
        # Rule 01 - prepare pairs in the plain text
        self.plaintext = plaintext

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
                
        
        for pair in plaintext_pairs:
            applied_rule = False
            
            # Rule 02 - Replace letters with their right letter in same row
            for row in key_matrix:
                if pair[0] in row and pair[1] in row:
                    row_index1 = row.find(pair[0])
                    row_index2 = row.find(pair[1])
                    
                    ciphertext_pair = row[(row_index1+1)%5] + row[(row_index2+1)%5] 
                    ciphertext_pairs.append(ciphertext_pair)
                    applied_rule = True
        
            if applied_rule:
                continue
                        
            # Rule 03 - Replace letters with their right letter in same column
            for j in range(5):
                col="".join([key_matrix[i][j] for i in range(5)])
                if pair[0] in col and pair[1] in col:
                        col_index1 = col.find(pair[0])
                        col_index2 = col.find(pair[1])
                        
                        ciphertext_pair = col[(col_index1+1)%5] + col[(col_index2+1)%5] 
                        ciphertext_pairs.append(ciphertext_pair)
                        applied_rule = True
                        
            if applied_rule:
                continue
            
            
            # Rule 04 - Replace letters with as the square that represent by pair
            row_index1 = 0
            row_index2 = 0
            col_index1 = 0
            col_index2 = 0
            
            for i in range(5):
                row=key_matrix[i]
                if pair[0] in row:
                    row_index1 = i
                    col_index1 = row.find(pair[0])
                
                if pair[1] in row:
                    row_index2 = i
                    col_index2 = row.find(pair[1])
            
            ciphertext_pair=key_matrix[row_index1][col_index2]+key_matrix[row_index2][col_index1]
            ciphertext_pairs.append(ciphertext_pair)
            
            ciphertext = "".join(ciphertext_pairs)
        print('Ciphertext is :',ciphertext.upper())
        
        
        
    # def encrypt(self, plaintext):
    #     encrypted_text = plaintext
    #     return encrypted_text
    
    # def decrypt(self, ciphertext):
    #     decrypted_text = ciphertext
    #     return decrypted_text 

def main():
    while True:
        print("====================================================================")
        key = input('Enter the Keyword :')                            
        choice = input("Enter 'E' to encrypt or 'D' to decrypt :") 
        
        if choice == 'E':                                   
            plaintext = input("Enter the text to encrypt: ")
            ciphertext = PlayfairCipher_Encryption(key,plaintext)            
            
        # elif choice == 'D':                                 # If user chooses decryption
        #     ciphertext = input("Enter the text to decrypt: ") # Take user input for the text to decrypt
        #     decrypted_text = cipher.decrypt(ciphertext)     # Decrypt the input text using the created cipher
        #     print("Decrypted:", decrypted_text)             # Display the decrypted text
            
        # else:
        #     print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")  # Handle invalid input
            
if __name__ == "__main__":
    main()                                                  # Call the main function when the script is executed