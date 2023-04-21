#Define Vigenere class
class Vigenere:
    def __init__(self, message, keyword):
        self.message = message.upper()
        self.keyword = keyword.upper()

#Create a method that checks if the length of both the message and keyword are equal
    def append_key(self):
        key = list(self.keyword)
        if len(self.message) == len(key):
            return key
        #Repeat the character of keywords if length are not equal
        #Use the modulo % to ensure that the length is finally equal
        else:
            key += [key[i % len(key)] for i in range(len(self.message) - len(key))]
        return key

#Create another method to encrypt the message by appending the keyword characters' values
    def encrypt(self):
        key = self.append_key()
        #Encrypt each letter in the message using character from keyword
        #Note that 65 is 'A' in ASCII
        encrypted_chars = (chr((ord(self.message[i]) + ord(key[i])) % 26 + 65)
                            #Check if the characters are alphabetic characters
                            if self.message[i].isalpha()
                            else self.message[i]
                            for i in range(len(self.message)))
        return ''.join(encrypted_chars)

#Prompt the user to input their message and keyword
message = input("\033[32mEnter the message:\033[0m ")
keyword = input("\033[33mEnter your keyword:\033[0m ")

#Add an instance
Vigenere1 = Vigenere(message, keyword)
encrypted_instance = Vigenere1.encrypt()

#Print the output
print("\033[1;31;43mEncrypted message: ", encrypted_instance + "\033[0m")