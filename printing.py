#since inputs are recycled, make them recombine each time they are needed
enter = 'Please enter name #'
enter_first = enter + '1: '
enter_second = enter + '2: '
enter_third = enter + '3: '
#user input for first name
name_first = input(enter_first)
#user input for second name
name_second = input(enter_second)
#user input for the third name
name_third = input(enter_third)
#one line gap
print()
#Title for results
print('Here are your names in every possible order:')
print('--------------------------------------------')
print()
#first 3 horizontal style
print('1. ' ,end='')
print(name_first, name_second, name_third, sep = ', ')
#one line gap
print()
#second list
print('2. ' ,end='')
print(name_first, name_third, name_second, sep = ', ')
#line gap
print()
#third list
print('3. ' ,end='')
print(name_second, name_first, name_third, sep = ', ')
#line gap
print()
#fourth combination, in a stack
print('4.' ,name_second)
print(name_third)
print(name_first)
#line gap
print()
#fifth and sixth lines in stacks
print('5.', name_third)
print(name_second)
print(name_first)
print()
print('6.', name_third)
print(name_first)
print(name_second)

