def encrypt(string):
    ciphertext = ""
    ciphertext = str(ciphertext)
    string = str(string)
    string = string.upper()
    for i in range(len(string)):
        char = string[i]
        charactercode = int(ord(char))
        if charactercode < 88 and charactercode > 64:
            ciphertext = ciphertext + chr(ord(char) + int(shiftvalue))
        elif charactercode >= 88 and charactercode <= 90:
            ciphertext = ciphertext + chr(ord(char) - 26 + int(shiftvalue))
        else:
            ciphertext = ciphertext + str(char)
    return ciphertext


def decrypt(string):
    ciphertext = ""
    ciphertext = str(ciphertext)
    string = str(string)
    string = string.upper()
    for i in range(len(string)):
        char = string[i]
        charactercode = int(ord(char))
        if charactercode > (64 + int(shiftvalue)) and charactercode < (88 + int(shiftvalue)):
            ciphertext = ciphertext + chr(ord(char) - int(shiftvalue))
        elif charactercode >= (62 + int(shiftvalue)) and charactercode <= (64 + int(shiftvalue)):
            ciphertext = ciphertext + chr(ord(char) + 26 - int(shiftvalue))
        else:
            ciphertext = ciphertext + str(char)
    return ciphertext


print("Note that if incorrect values are inputted, the program will crash")
string = input("plain text: ")
shiftvalue = input("shift value: ")
mode = input("input 1 for encrypt, input 2 for decrypt: ")
mode = int(mode)

if mode==1:
    print("Plain Text: " + string + "     Cipher Text: " + encrypt(string))
    string = "meet"
    print("Plain Text: " + string + "     Cipher Text: " + encrypt(string))
    string = "me"
    print("Plain Text: " + string + "     Cipher Text: " + encrypt(string))
    string = "after"
    print("Plain Text: " + string + "     Cipher Text: " + encrypt(string))
    string = "party"
    print("Plain Text: " + string + "     Cipher Text: " + encrypt(string))
    closeprogram = input("Press enter to exit program")
elif mode==2:
    print("Cipher Text: " + string + "     Plain Text: " + decrypt(string))
    string = "PHHW"
    print("Cipher Text: " + string + "     Plain Text: " + decrypt(string))
    string = "PH"
    print("Cipher Text: " + string + "     Plain Text: " + decrypt(string))
    string = "DIWHU"
    print("Cipher Text: " + string + "     Plain Text: " + decrypt(string))
    string = "SDUWB"
    print("Cipher Text: " + string + "     Plain Text: " + decrypt(string))
    closeprogram = input("Press enter to exit program")
else:
    closeprogram = input("No mode chosen, press enter to exit program")
