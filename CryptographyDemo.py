from cryptography.fernet import Fernet
import rsa

# Symmetric encryption
# First, define the message to be encrypted.
message1 = "This message is encrypted using symmetric encryption"

# Generate the key and assign it to a variable.
key = Fernet.generate_key()
fernet = Fernet(key)

# Encrypt the message using the key.
encryptedMessage = fernet.encrypt(message1.encode())

# Print the key and then both messages.
print("Key: ", key)
print("Original: ", message1)
print("Encrypted: ", encryptedMessage)

# Decrypt the encrypted message and print it.
decryptedMessage = fernet.decrypt(encryptedMessage).decode()
print("Decrypted: ", decryptedMessage)

# Divider
print("----------------------------------------------------------")

# Asymmetric encryption
# Define a new message.
message2 = "This message is encrypted using asymmetric encryption"

# Generate public and private keys.
publicKey, privateKey = rsa.newkeys(512)

# Encrypt the original message asymmetrically.
asymEncryptedMessage = rsa.encrypt(message2.encode(), publicKey)

# Print the keys
print("Public Key: ", publicKey)
print("Private Key: ", privateKey)

# Print both the original and encrypted messages.
print("Original: ", message2)
print("Encrypted: ", asymEncryptedMessage)

# Decrypt the message using the private key.
asymDecryptedMessage = rsa.decrypt(asymEncryptedMessage, privateKey).decode()

# Print the decrypted message.
print("Decrypted: ", asymDecryptedMessage)