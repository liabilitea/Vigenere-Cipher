# Vigenere-Cipher
* * *

## Description

This Python project encrypts a message inputted by the user using the Vinegere Cipher, which employs a keyword to perform the encryption of messages by shifting every plaintext letter by a corresponding keyword letter. Moreover, this code uses the Object - Oriented approach by defining a class with two parameters and two methods. 

### Breakdown of Methods Used

+ Append Method

    The code below checks whether the lengths of the message and keyword are equal; if they are, it returns the keyword as a list. If not, the code repeats the characters of the keyword to match the length of the message.
    
    ```
  def append_key(self):
        key = list(self.keyword)
        if len(self.message) == len(key):
            return key
        else:
            key += [key[i % len(key)] for i in range(len(self.message) - len(key))]
        return key
    ```
    
+ Encrypt Method

    The code below encrypts every letter of the message by utilizing the keyword's characters. The ASCII values of the characters are utilized to carry out the encryption process, and the encrypted message is returned as a string.
    
    ```
  def encrypt(self):
        key = self.append_key()
        encrypted_chars = (chr((ord(self.message[i]) + ord(key[i])) % 26 + 65)
                            if self.message[i].isalpha()
                            else self.message[i]
                            for i in range(len(self.message)))
        return ''.join(encrypted_chars)
    ```
 
## How To Use / Run 

1. Install Python on your computer to run the code. You can download its latest version here: https://www.python.org/downloads/
2. Copy the code from the repository. 
3. Open an IDE and paste the code.
    + If you don't have an IDE, you can use any text editor from your computer and paste the code. 
4. Save the file with a .py extension.
5. Run the code.
    + For text-editor users, open a command prompt or terminal window and locate the folder where the Python file was saved and enter the command provided below by typing it in the command-line interface. After typing the command, press the Enter key to execute.
    
  ```
  python 'file_name'.py
  ```
6. It will ask you to enter a message and a keyword. Press Enter after inputting your message and after you input your keyword.
7. The encrypted text will be displayed in all uppercase letters. 

## Example Output

  **Note** that the output is all uppercase because the message input is converted to uppercase inside the Vigenere class's init method using the upper() method.
  
  ```
  Enter the message: LETSGOTOTHESHOW
  Enter your keyword: ticket
  Encrypted message:  EMVCKHMWVRILAWY
  ```
