import string

class RailFence_Encryption:
    def __init__(self, key,plaintext):
        ciphertext = ""   
        cycle = key * 2 - 2
        
        for row in range(key):
            index = 0
            
            #first row
            if row == 0:
                while index < len(plaintext):
                    ciphertext+=plaintext[index]
                    index+=cycle
            
            #last row
            elif row == key - 1:
                index = row
                while index < len(plaintext):
                    ciphertext+=plaintext[index]
                    index+=cycle
                
            #intermidiate rows
            else:
                left_index = row
                right_index = cycle - row
                while left_index < len(plaintext):
                    ciphertext+=plaintext[left_index]
                    
                    if right_index < len(plaintext):
                        ciphertext+=plaintext[right_index]
                    
                    left_index+=cycle
                    right_index+=cycle
        
        print(ciphertext)
           

def main():
    while True:
        print("====================================================================")
        key = int(input('Enter the Keyword :'))                            
        choice = input("Enter 'E' to encrypt or 'D' to decrypt :")
        
        if choice == 'E':                                   
            plaintext = input("Enter the text to encrypt: ")
            ciphertext = RailFence_Encryption(key,plaintext)            
            
        # elif choice == 'D':                                   
        #     ciphertext = input("Enter the text to decrypt: ")
        #     plaintext = RailFence_Decryption(key,ciphertext)           
            
        # else:
        #     print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
            
if __name__ == "__main__":
    main()       
                                               
    # this is top secret
    # 4
    # 