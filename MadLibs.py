'''
    Mad Libs are activities that have a person provide various words, which are
    then used to complete a short story in unexpected (and hopefully funny) ways.

    Write a program that takes a string and an integer as input, and outputs a
    sentence using the input values as shown in the example below. The program
    repeats until the input string is quit and disregards the integer input that follows.

        Ex: If the input is:
            apples 5
            shoes 2
            quit 0
        the output is:
            Eating 5 apples a day keeps the doctor away.
            Eating 2 shoes a day keeps the doctor away.
'''
flag = True

while flag:
    inp = input('Enter a sentence: ')

    separated = inp.split(' ')
    item = separated[0]
    num = separated[1]

    if item == 'quit':
        flag = False
        break

    print(f'Eating {num} {item} a day keeps the doctor away.')

