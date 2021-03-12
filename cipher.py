from string import ascii_uppercase, ascii_lowercase
import re

class CaesarCipher:
    def __init__(self, message, shift, choice):
        self.message = message
        self.shift  = shift % 26
        if re.search("(d|D)(e|E)(c|C)(o|O)(d|D)(e|E)", choice):
            self.shift *= -1

    def encode_decode(self):
        result = ""

        for char in self.message:    
            if char.isalpha():

                if 65 <= ord(char) <= 90:
                    new_char = ascii_uppercase[(self.shift + ascii_uppercase.index(char)) % 26]
                else:
                    new_char = ascii_lowercase[(self.shift + ascii_lowercase.index(char)) % 26]

                result += new_char
                
            else:
                result += char

        return result

