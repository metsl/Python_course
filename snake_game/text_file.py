with open("my_file.txt", mode="a") as file:
    file.read()
    print(contents)
    contents = file.write("This line has been added but the function Write")
    print(contents)