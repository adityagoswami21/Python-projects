from morse import morse
def text_to_morse(text):
    morse_code = ""
    for i in text.upper():
        if i in morse:
            morse_code += morse[i] + " "
    return morse_code
while True:
    text = input("Enter text to convert to Morse code: ")
    if text == "exit":
        print("Exiting program.")
        break
    print("Morse code:", text_to_morse(text))

