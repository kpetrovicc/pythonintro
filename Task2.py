# **** Cheat Sheet of used fuctions ****
#.upper() - converts string to uppercase
#.lower() - converts string to lowercase
#.isupper() - checks if string is uppercase
#.islower() - checks if string is lowercase
#.len() - returns length of string
#The example would be: print(len(phrase)) - it would return 15
#.index() - returns index of character
#The example would be: print(phrase.index("G")) - it would return 0
#.replace() - replaces string with another string
#The example would be: print(phrase.replace("Giraffe", "Elephant")) - it would return Elephant Academy
#This one takes in two arguments, the first one is the string you want to replace, and the second one is the string you want to replace it with

phrase = "Giraffe Academy"
print(phrase.replace(" ", "Elephant"))