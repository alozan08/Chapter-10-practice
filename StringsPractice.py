# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
    print(mystring[:x])


# expected output: WGU
printFirst('WGU College of IT', 3)

# expected output: WGU College
printFirst('WGU College of IT', 11)

############################################################################################################

# Complete the function to return the last X number of characters
# in the given string


def getLast(mystring, x):
    return mystring[-x:]


# expected output: IT
print(getLast('WGU College of IT', 2))

# expected output: College of IT
print(getLast('WGU College of IT', 13))

############################################################################################################

# Complete the function to return True if the word WGU exists in the given string
# otherwise return False


def containsWGU(mystring):
    if 'WGU' in mystring:
        return True
    else:
        return False


# expected output: True
print(containsWGU('WGU College of IT'))

# expected output: False
print(containsWGU('Night Owls Rock'))

############################################################################################################

# Complete the function to print all of the words in the given string


def printWords(mystring):
    mystring_split = mystring.split(' ')
    print(mystring_split)


# expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')

# expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')

############################################################################################################

# Complete the function to replace the word WGU with Western Governors University
# and print the new string
def replaceWGU(mystring):
    print(mystring.replace('WGU', 'Western Governors University'))

# expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')

# expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')

############################################################################################################

# Complete the function to remove the word WGU from the given string
# ONLY if it's not the first word and return the new string
def removeWGU(mystring):
    if mystring[0:3] == 'WGU':
        return mystring
    else:
        return mystring.replace('WGU', '')

# expected output: WGU Rocks
print(removeWGU('WGU Rocks'))

# expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))#

############################################################################################################

# Complete the function to remove trailing spaces from the first string
# and leading spaces from the second string and return the combined strings
def removeSpaces(string1, string2):
    combined = string1.rstrip() + string2.lstrip()
    return combined

# expected output: WGU Rocks-You know it!
print(removeSpaces('WGU Rocks    ', '  -You know it!'))

# expected output: Welcome WGU-IT Students
print(removeSpaces('Welcome WGU ', ' -IT Students'))

############################################################################################################

# Complete the function to print the specified hourly rate with two decimals
def displayHourlyRate(rate):
    print(f'${rate:.2f}')

# expected output: $34.79
displayHourlyRate(34.789123)

# expected output: $24.12
displayHourlyRate(24.123456)

############################################################################################################

# Complete the function to return the number of uppercase letters in the given string
def countUpper(mystring):
    count = 0
    for letter in mystring:
        if letter.isupper():
            count += 1

    return count

# expected output: 4
print(countUpper('Welcome to WGU'))

# expected output: 2
print(countUpper('Hello, Mary'))
