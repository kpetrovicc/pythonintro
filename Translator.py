# Build a translator

vowels = "aeiou"

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in vowels:
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase: ")))