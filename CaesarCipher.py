def encode(plaintext, key):
    #Chars = characters
    plaintextChars = [str(character) for character in plaintext]
    #print(plaintextChars)
    #Ints = integers
    plaintextInts = [ord(character) for character in plaintextChars]
    #print(plaintextInts)
    ciphertextInts = []
    for integer in plaintextInts:
        if(key >= 0):
            if (integer >= 97) and (integer <=122):
                if((integer+key) > 122):
                    integer = integer + key - 26
                else:
                    integer = integer + key
            if (integer >= 65) and (integer <= 90):
                if((integer+key) > 90):
                    integer = integer + key - 26
                else:
                    integer = integer + key
        else:
            if (integer >= 97) and (integer <=122):
                if((integer+key) < 97):
                    integer = integer + key + 26
                else:
                    integer = integer + key
            if (integer >= 65) and (integer <= 90):
                if((integer+key) < 65):
                    integer = integer + key + 26
                else:
                    integer = integer + key
        ciphertextInts.append(integer)
    #print(ciphertextInts)
    ciphertextChars = [chr(integer) for integer in ciphertextInts]
    #print(ciphertextChars)
    ciphertext = "".join(ciphertextChars)
    return ciphertext

def decode(ciphertext, key):
    #Chars = characters
    ciphertextChars = [str(character) for character in ciphertext]
    #print(ciphertextChars)
    #Ints = integers
    ciphertextInts = [ord(character) for character in ciphertextChars]
    #print(ciphertextInts)
    plaintextInts = []
    for integer in ciphertextInts:
        if(key >= 0):
            if (integer >= 97) and (integer <=122):
                if((integer-key) < 97):
                    integer = integer - key + 26
                else:
                    integer = integer - key
            if (integer >= 65) and (integer <= 90):
                if((integer-key) < 65):
                    integer = integer - key + 26
                else:
                    integer = integer - key
        else:
            if (integer >= 97) and (integer <=122):
                if((integer-key) > 122):
                    integer = integer - key - 26
                else:
                    integer = integer - key
            if (integer >= 65) and (integer <= 90):
                if((integer-key) > 90):
                    integer = integer - key - 26
                else:
                    integer = integer - key
        plaintextInts.append(integer)
    #print(plaintextInts)
    plaintextChars = [chr(integer) for integer in plaintextInts]
    #print(plaintextChars)
    plaintext = "".join(plaintextChars)
    return plaintext

def cipherLoop():
    print("Use Caesar cipher to encrypt or decrypt messages.")
    print("1.Decrypt message")
    print("2.Encrypt message")
    key = 26
    choice = int(input("Choose (1 or 2):"))
    if (choice == 1):
        ciphertext = input("Enter message to decrypt:")
        while not int(key) in range(-25,26):
            key = int(input("Key can have any value from 25 to -25. Enter key:"))
        plaintext = decode(ciphertext, key)
        print("Decrypted message is '" + plaintext + "'" )
    elif (choice == 2):
        plaintext = input("Enter message to encrypt:")
        while not int(key) in range(-25,26):
            key = int(input("Key can have any value from 25 to -25. Enter key:"))
        ciphertext = encode(plaintext, key)
        print("Encrypted message is '" + ciphertext + "'")
    else:
        print("Invalid choice")

choice_yn = 'y'
while (choice_yn == 'y') or (choice_yn == 'Y'):
    cipherLoop()
    choice_yn = input("Do you want to do it again(y/n):")







    


