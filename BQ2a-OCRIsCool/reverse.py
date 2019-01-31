f = open('text.txt', 'r')

inputStr = f.read()

inputList = list(inputStr)

f.close()

o = open('decrypt.txt', 'w')

for shift in range(27):
    tempStr = inputList
    for index, char in enumerate(tempStr):

        if char.isalpha() and char.islower():
            charNum = ord(char) - 97
            shiftedNum = (charNum - shift)%26
            if shiftedNum < 0:
                shiftedNum = shiftedNum + 25

            shiftedChar = chr(shiftedNum + 97)

            tempStr[index] = shiftedChar
        elif char.isalpha() and char.isupper():
            charNum = ord(char) - 65
            shiftedNum = (charNum - shift)%26
            if shiftedNum < 0:
                shiftedNum = shiftedNum + 25
                
            shiftedChar = chr(shiftedNum + 65)

            tempStr[index] = shiftedChar
    
    output = ''.join(tempStr)
    if 'CTF{' in output:
        print(output)
        o.write(output)
        exit()