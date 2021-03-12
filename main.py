from cipher import CaesarCipher

is_replay = True

while is_replay:
    choice = input("Type:\n> 'encode' to encrypt\n> 'decode' to decrypt\nInput : ")
    text = input("\nType your message:\n> ")
    shift = int(input("Type the shift number:\n> "))

    result = CaesarCipher(text, shift, choice)
    print("\nResult:\n> ", result.encode_decode())

    is_replay = True if input("\nDo you want to restart this program? (yes/no)\n> ") == "yes" else False
