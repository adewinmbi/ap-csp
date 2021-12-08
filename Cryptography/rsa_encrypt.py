import rsa as rsa

key = input("Enter the Encryption Key: " )
mod_value = input("Enter the Modulus: " )
plaintext = input("Enter a message to encrypt: ")

while True:
  if (key.isdigit() and mod_value.isdigit()):
    encrypted_msg = rsa.encrypt(int(key), int(mod_value), plaintext)
    print("Encrypted Message:", encrypted_msg)
  else:
    print("Key or modulus value contained letters or symbols. Please enter digits only.")
    key = input("Enter the Encryption Key: " )
    mod_value = input("Enter the Modulus: " )
    plaintext = input("Enter a message to encrypt: ")