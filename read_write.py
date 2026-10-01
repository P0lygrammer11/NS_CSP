#NS, read and writing to files

with open("practice.txt", "r+") as file:            # "with open" the key words to open the file    #"r+" lets you read and write
    # "practice.txt" is the file path (location )
    # "r" is what we do with this file, in this example its (r) reading it
    # as file, is us naming it so we can access it.
    content = file.read()           # gives you whats in the file.
    content = "chapter 1:\n" + content + "And christopher robin was sitting on his doorstep outting on his big boots"  #"\n" puts it on a new line
    file.write(content)          #content is a string
    with open("practice.txt" , "a") as file: #"w" stands for write              # "a" stands for apend and it adds content to the end. 
        file.write("\nwinnie the pooh and the blustary day") # it replaces the content

