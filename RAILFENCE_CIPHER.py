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
           
class RailFence_Decryption:
    def __init__(self, key,ciphertext):
        length = len(ciphertext)
        plaintext = "." * length
        cycle = 2 * key - 2
        units = length // cycle
        rail_lengths = [0] * key
        
        # Top Rail Length
        rail_lengths[0] = units
        
        # Intermidiate Rail length
        for i in range(1, key - 1):
            rail_lengths[i] = 2 * units
            
        # Bottom Rail length
        rail_lengths[key - 1] = units
        
        for i in range(length % cycle):
            if i < key:
                rail_lengths[i] += 1
            
            else:
                rail_lengths[cycle - i] += 1
        
        print(rail_lengths)
        
        # Replace characters in the top rail
        index = 0
        rail_offset = 0
        for c in ciphertext[:rail_lengths[0]]:
            plaintext = plaintext[:index] + c + plaintext[index + 1 :]
            index+=cycle
        rail_offset += rail_lengths[0]
        print(plaintext)
        
        # Replace characters in the intermidiate rail
        for row in range(1, key - 1):
            left_index = row
            right_index = cycle - row
            left_char = True
            
            for c in ciphertext[rail_offset:rail_offset + rail_lengths[row]]:
                if left_char:
                    plaintext = plaintext[:left_index] + c + plaintext[left_index+1:]
                    left_index+=cycle
                    left_char = not left_char
                
                else:
                    plaintext = plaintext[:right_index] + c + plaintext[right_index+1:]
                    right_index += cycle
                    left_char = not left_char
            
            rail_offset += rail_lengths[row]
            print(plaintext)
            
        
        # Replace characters in the last rail
        index = key - 1
        for c in ciphertext[rail_offset:]:
            plaintext = plaintext[:index] + c + plaintext[index + 1 :]
            index+=cycle

        print(plaintext)
        
def main():
    while True:
        print("====================================================================")
        key = int(input('Enter the Keyword :'))                            
        choice = input("Enter 'E' to encrypt or 'D' to decrypt :")
        
        if choice == 'E':                                   
            plaintext = input("Enter the text to encrypt: ")
            ciphertext = RailFence_Encryption(key,plaintext)            
            
        elif choice == 'D':                                   
            ciphertext = input("Enter the text to decrypt: ")
            plaintext = RailFence_Decryption(key,ciphertext)           
            
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
            
if __name__ == "__main__":
    main()       
                                               
    # this is top secret
    # 4
    # tsshi  eti tpcesor