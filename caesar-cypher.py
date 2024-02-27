# Create a custom function that concatenates a string with itself:
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
# Testing the previous function:
#alphabet = input("Enter some part of the alphabet: ")
#print(getDoubleAlphabet(alphabet))

# Define a function that requests a message to encrypt from the user:
def getMessage():
    stringToEncrypt = input("Enter a message to encrypt: ")
    return stringToEncrypt
    
# Define a function to request a cypher key from the user:
def getCypherKey():
    shiftAmount = input("Enter a key (whole number between 1-25): ")
    return shiftAmount
    
# Define the encryption function:
def encryptMessage(message, cypherKey, alphabet):
    # Initialize variables:
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    # Traverse each letter in the mesage:
    for currentCharacter in uppercaseMessage:
        # Find the position of the letter:
        position = alphabet.find(currentCharacter)
        # Determine the new position with the cipherKey:
        newPosition = position + int(cypherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# Define a decryption function using the previous encryption function:
def decryptMessage(message, cypherKey, alphabet):
    decryptKey = -1 * int(cypherKey)
    return encryptMessage(message, decryptKey, alphabet)
    
# Define a function for the main logic of the program:
def runCaesarCypherProgram():
    myAlphabet = "ABCDEFGGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'myAlphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCypherKey = getCypherKey()
    print(myCypherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCypherKey, myAlphabet2)
    print(f'myEncryptedMessage: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCypherKey, myAlphabet2)
    print(f'myDecryptedMessage: {myDecryptedMessage}')
    
# Run the previously defined function
runCaesarCypherProgram()

    