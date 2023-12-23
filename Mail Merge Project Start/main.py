# opening the starting_letter.txt file
with open("./Input/Letters/starting_letter.txt", "r") as letter:
    # modifying the letter in list form into a readable letter
    f = "".join(letter)
    print(f)
