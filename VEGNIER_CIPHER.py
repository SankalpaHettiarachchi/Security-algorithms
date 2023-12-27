import string

# Encryption Class----------------------------------------------------------------------------------------------       
class VegnierCipher_Encryption:
    def __init__(self, key,plaintext):
        ciphertext = ''
        index = 0
        for c in plaintext:
            if c in string.ascii_lowercase:
                offset = ord(key[index])-ord('a')
                encrypted_c = chr((ord(c) - ord('a') + offset) % 26 + ord('a'))
                ciphertext = ciphertext + encrypted_c
                index=(index+1)%len(key)
                
            else:
                ciphertext=ciphertext + c
                
        print('Plaintext is   :',plaintext)
        ciphertext = ciphertext.upper()
        print('Ciphertext is  :',ciphertext)
        
# Decryption Class----------------------------------------------------------------------------------------------       
class VegnierCipher_Decryption:
    def __init__(self, key,ciphertext):
        plaintext = ''
        index = 0
        lower_ciphertext = ciphertext.lower()
        for c in lower_ciphertext:
            if c in string.ascii_lowercase:
                offset = ord(key[index]) - ord('a')
                positve_offset = 26 - offset
                
                decrypted_c = chr((ord(c) - ord('a') + positve_offset) % 26 + ord('a'))
                plaintext = plaintext + decrypted_c
                index=(index+1)%len(key)
                
            else:
                plaintext=plaintext + c
                
        print('Ciphertext is  :',ciphertext)
        print('Plaintext is   :',plaintext)

def main():
    while True:
        print("====================================================================")
        key = input('Enter the Keyword :')                            
        choice = input("Enter 'E' to encrypt or 'D' to decrypt :")
        
        if choice == 'E':                                   
            plaintext = input("Enter the text to encrypt: ")
            ciphertext = VegnierCipher_Encryption(key,plaintext)            
            
        elif choice == 'D':                                   
            ciphertext = input("Enter the text to decrypt: ")
            plaintext = VegnierCipher_Decryption(key,ciphertext)           
            
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
            
if __name__ == "__main__":
    main()       
                                               
    # the quick brown fox jumps over the lazy dog
    # lemon
    # ELQ EHTGW PEZAZ TBI NGACD SHSE ELQ ZNKC PCT
