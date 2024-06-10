def generate_keyword(text, keyword):
    keyword = list(keyword)
    if len(text) == len(keyword):
        return keyword
    else:
        for i in range(len(text) - len(keyword)):
            keyword.append(keyword[i % len(keyword)])
    return "".join(keyword)

def vigenere_encrypt(plaintext, keyword):
    keyword = generate_keyword(plaintext, keyword)
    encrypted_text = []
    for p, k in zip(plaintext, keyword):
        if p.isalpha():
            shift_base = 65 if p.isupper() else 97
            shift = 65 if k.isupper() else 97
            encrypted_char = chr((ord(p) + ord(k) - 2 * shift_base) % 26 + shift_base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(p)
    return "".join(encrypted_text)

def vigenere_decrypt(ciphertext, keyword):
    keyword = generate_keyword(ciphertext, keyword)
    decrypted_text = []
    for c, k in zip(ciphertext, keyword):
        if c.isalpha():
            shift_base = 65 if c.isupper() else 97
            shift = 65 if k.isupper() else 97
            decrypted_char = chr((ord(c) - ord(k) + 26) % 26 + shift_base)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(c)
    return "".join(decrypted_text)

def main():
    print("Vigenère Cipher Encryption and Decryption")
    
    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            keyword = input("Enter the keyword: ")
            ciphertext = vigenere_encrypt(plaintext, keyword)
            print(f"Encrypted Text: {ciphertext}")
        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            keyword = input("Enter the keyword: ")
            plaintext = vigenere_decrypt(ciphertext, keyword)
            print(f"Decrypted Text: {plaintext}")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
