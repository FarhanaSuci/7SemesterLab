'''
Advance Encryption Standard By Priyo.

For this code install pycrytodome first

To do this simply type the following in terminal:
    pip install pycryptodome


'''

from Crypto.Random import get_random_bytes # for key generation
from Crypto.Protocol.KDF import PBKDF2 # for preventing bruteforce attack

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad


# key generation--> generating 32 bytes key

simple_key = get_random_bytes(32)
print("\n\nThe output that we get:\n"+ str(simple_key))

password = "mypassword"

key = PBKDF2(password, simple_key, dkLen=32)
print("\n\nOur actual key:\n"+str(key))

#----------key generation ends-------------

#Encryption process starts here

message = b"Hello group B. Group B Rocks!!!"
print("\n\nThis is our message after converting it to bytes:\n"+str(message))


cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

print("\n\nThis is our encrypted data:\n"+ str(ciphered_data))

# sir jodi bole onno file e save koro cipher text ke

with open('encrypted.bin','wb') as f: # bytes data ke binary file e save korbo
    f.write(cipher.iv)
    f.write(ciphered_data)


#------Encryption ends here----------------------

# Decryption process starts here

# sir jodi bole file theke input naw

with open('encrypted.bin','rb') as f: 
    iv = f.read(16)
    ciphered_data = f.read()


cipher = AES.new(key, AES.MODE_CBC,iv)
original_msg = unpad(cipher.decrypt(ciphered_data),AES.block_size)

print("\n\nThe original Message is:\n"+ str(original_msg))

#--------Decryption ends here-----------
print("\n\n\nThe program has ended")





