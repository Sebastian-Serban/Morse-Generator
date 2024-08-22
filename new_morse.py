# Morse code encoder and decoder programm


# The Morse code dictionary
morseAlphabet= {"A" : ".-" ,
                "Ä" : "·-·-",
                "B" : "-...",
                "C" : "-.-.",
                "D" : "-..",
                "E" : "." ,
                "F" : "..-." ,
                "G" : "--." ,
                "H" : "...." ,
                "I" : ".." ,
                "J" : ".---" ,
                "K" : "-.-" ,
                "L" : ".-.." ,
                "M" : "--" ,
                "N" : "-." ,
                "O" : "---" ,
                "Ö" : "---·", 
                "P" : ".--." ,
                "Q" : "--.-" ,
                "R" : ".-." ,
                "S" : "..." ,
                "T" : "-" ,
                "U" : "..-" ,
                "Ü" : "··--",
                "V" : "...-" ,
                "W" : ".--" ,
                "X" : "-..-" ,
                "Y" : "-.--" ,
                "Z" : "--..",
                "0" : "-----",
                "1" : ".----",
                "2" : "..---",
                "3" : "...--",
                "4" : "....-",
                "5" : ".....",
                "6" : "-....",
                "7" : "--...",
                "8" : "---..",
                "9" : "----."}

letters = {morseAlphabet[l] : l for l in morseAlphabet.keys()}

# Help for the programm variables
# chiper =  the encoded message
# decipher = the decoded message
# message = the original message
# spaces = the number of spaces between word


def encodeMessage(msg):
    cipher = ''
    for letter in msg:
        if letter == ' ':
            cipher += ' '
        else:
            cipher += morseAlphabet[letter] + ' '
    return cipher + ' '

def decodeMessage(encmsg):
    decipher = ''
    parseCode = ''
    spaces = 0
    for code in encmsg:
        if code != ' ':
            spaces = 0
            parseCode += code
        else:
            spaces += 1
            if spaces == 2:
                decipher += ' '
            else:
                decipher += letters[parseCode]
                parseCode = ''

    return decipher.capitalize()

def main():
    message = "Mit einer neuen Studie"
    enc_message = encodeMessage(message.upper())
    print(enc_message)

    # dec_message = decodeMessage(enc_message)
    # print(dec_message)




if __name__ == '__main__':
    main()
