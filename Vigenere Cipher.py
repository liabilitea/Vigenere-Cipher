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


#Prompt the user to input their message and keyword
#Print the output