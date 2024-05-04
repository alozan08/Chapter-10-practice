'''
    Many documents use a specific format for a person's name. Write a program whose input is:
        firstName middleName lastName
    and whose output is:
        lastName, firstInitial.middleInitial.

    Ex: If the input is:
        Pat Silly Doe
    the output is:
        Doe, P.S.

    If the input has the form:
        firstName lastName
    the output is:
        lastName, firstInitial.

    Ex: If the input is:
        Julia Clark
    the output is:
        Clark, J.
'''
name = input('Enter your full name: ')

separated = name.split(' ')
if len(separated) == 2:
    firstName = separated[0]
    lastName = separated[1]
    print(f'{lastName.title()}, {firstName[0].title()}.')
else:
    firstName = separated[0]
    middleName = separated[1]
    lastName = separated[2]
    print(f'{lastName.title()}, {firstName[0].title()}.{middleName[0].title()}.')

