'''
    Write a program that removes all non-alpha characters from the given input.
        Ex: If the input is:
            -Hello, 1 world$!
        the output is:
            Helloworld
'''

def RemNonAlphaChar(input):
    result = ''
    for char in input:
        if char.isalpha():
            result += char
    return result

userInput = input("Enter a sentence with non-alpha characters: ")
print(RemNonAlphaChar(userInput))