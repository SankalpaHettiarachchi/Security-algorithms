import math

class Columnar_Encryption:
    def __init__(self, key,plaintext):
        ciphertext = ""
        k_indx = 0
        msg_len = float(len(plaintext))
        msg_lst = list(plaintext)
        key_lst = sorted(key)

        col = len(key)
        row = int(math.ceil(msg_len / col))
        fill_null = int((row * col) - msg_len)
        msg_lst.extend('_' * fill_null)

        matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])
            ciphertext += ''.join([row[curr_idx] for row in matrix])
            k_indx += 1
            
        print(ciphertext)


class Columnar_Decryption:
    def __init__(self, key,ciphertext):
        msg_indx = 0
        k_indx = 0
        msg_len = float(len(ciphertext))
        msg_lst = list(ciphertext)
        col = len(key)
        row = int(math.ceil(msg_len / col))
        key_lst = sorted(key)

        dec_cipher = []
        for _ in range(row):
            dec_cipher += [[None] * col]

        for _ in range(col):
            curr_idx = key.index(key_lst[k_indx])

        
            for j in range(row):
                dec_cipher[j][curr_idx] = msg_lst[msg_indx-1]
                msg_indx += 1
            k_indx += 1
            
        plaintext = ''.join(sum(dec_cipher, []))
        null_count = plaintext.count('_')

        if null_count > 0:
            return plaintext[: -null_count]
        
        print(plaintext)
        

def main():
    while True:
        print("====================================================================")
        key = input('Enter the Keyword :')                       
        choice = input("Enter 'E' to encrypt or 'D' to decrypt :")
        
        if choice == 'E':                                   
            plaintext = input("Enter the text to encrypt: ")
            ciphertext = Columnar_Encryption(key,plaintext)            
            
        elif choice == 'D':                                   
            ciphertext = input("Enter the text to decrypt: ")
            plaintext = Columnar_Decryption(key,ciphertext)           
            
        else:
            print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
            
if __name__ == "__main__":
    main()       
                                               
    # 
    # 
    # 