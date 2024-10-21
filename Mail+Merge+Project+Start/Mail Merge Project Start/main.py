#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
template_file = "./Input/Letters/starting_letter.txt"
names_file = "./Input/Names/invited_names.txt"

#opening Letter in write mode
with open(template_file, mode="r") as starting_letter:
    content_letter = starting_letter.read()

#opening list of names in read mode
with open(names_file, 'r') as invited_names:
    names = invited_names.readlines()
    print(names)

names = [name.strip() for name in names]
print(names)

#creating a new file for each name
for name in names:
    letter = content_letter.replace("[name]", name)
    filename = f'./Output/ReadyToSend/invitation_for_{name}.txt'
    with open(filename, 'w') as letter_file:
        letter_file.write(letter)