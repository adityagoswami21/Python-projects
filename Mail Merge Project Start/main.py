# opening the starting_letter.txt file
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    # modifying the letter in list form into a readable letter
    txt = "".join(letter)
# opening invited_names.txt file
with open("./Input/Names/invited_names.txt", "r") as n:
    # reading each name
    names = n.readlines()
for name in names:
    # replacing extra line from the letter
    name = name.rstrip("\n")
    # replacing [name] with actual names one by one
    x = txt.replace("[name]", name)
    # creating new files with respective name and entering their respective letters
    with open(f"./Output/ReadyToSend/{name}.txt", "w") as enter:
        enter.write(x)

