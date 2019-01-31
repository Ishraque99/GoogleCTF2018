# Caesar Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

message = open('text.txt', 'r').read()
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerLetters = LETTERS.lower()
o = open('decrypted.txt', 'w')
# loop through every possible key
for key in range(len(LETTERS)):

    # It is important to set translated to the blank string so that the
    # previous iteration's value for translated is cleared.
    translated = ''

    # The rest of the program is the same as the original Caesar program:

    # run the encryption/decryption code on each symbol in the message
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key

            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(LETTERS)

            # add number's symbol at the end of translated
            translated = translated + LETTERS[num]
        
        elif symbol in lowerLetters:
            num = lowerLetters.find(symbol) # get the number of the symbol
            num = num - key

            # handle the wrap-around if num is 26 or larger or less than 0
            if num < 0:
                num = num + len(lowerLetters)

            # add number's symbol at the end of translated
            translated = translated + lowerLetters[num]
        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol

    # display the current key being tested, along with its decryption
    output = ('Key #%s: %s' % (key, translated))
    o.write(output)