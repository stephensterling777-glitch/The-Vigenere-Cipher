#Cryptography 3: The Viginere Cipher
#Stephen Sterling
import string
import math

character_list=string.ascii_lowercase
message = input('Enter message: ')
key = input('Enter key: ')

def encrypt(message,key):
    encrypted_message = ''
    for i in range(len(message)):
        new_i = i % len(key)
        key_location = character_list.find(key[new_i])
        location = character_list.find(message[i])
        character_location = (key_location+location) % len(character_list)
        encrypted_message += character_list[character_location]
    return encrypted_message

def decrypt(message,key):
    encrypted_message = ''
    for i in range(len(message)):
        new_i = i % len(key)
        key_location = character_list.find(key[new_i])
        location = character_list.find(message[i])
        character_location = (location-key_location) % len(character_list)
        encrypted_message += character_list[character_location]
    return encrypted_message

print(encrypt(message,key))

        
    



