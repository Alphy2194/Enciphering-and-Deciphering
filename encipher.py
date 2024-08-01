def modular_inverse(a, n):
    """Find modular multiplicative inverse."""
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    return None

def encipher(text):
    """Encipher text using the given affine cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            x = ord(char) - ord('A')
            encrypted_char = (3 * x + 14) % 26
            result += chr(encrypted_char + ord('A'))
        else:
            result += char
    return result

def decipher(text):
    """Decipher text using the given affine cipher."""
    result = ""
    inverse_a = modular_inverse(3, 26)
    for char in text:
        if char.isalpha():
            y = ord(char) - ord('A')
            decrypted_char = (inverse_a * (y - 14)) % 26
            result += chr(decrypted_char + ord('A'))
        else:
            result += char
    return result

# Main program
def main():
    print("Affine Cipher Encryption and Decryption")
    print("--------------------------------------")
    name = input("Enter the name to be encrypted: ").upper()
    encrypted_name = encipher(name)
    print("Encrypted:", encrypted_name)

    decrypted_name = decipher(encrypted_name)
    print("Decrypted:", decrypted_name)

if __name__ == "__main__":
    main()
