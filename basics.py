print(3+2) # print some stuff

ripeness = 7
is_ripe = ripeness > 8 and ripeness <= 10 # combined boolean statements
# conditional
if is_ripe:
    print('Let\'s have this goodie !')
else:
    print('Oh, no!')

print(5*'supeR')

print(type(5))

num_str = "3.4"
print(type(float(num_str))) # string becomes a float
num = 3.4
print(str(num) + ' is a respectable number')

print(type(len("superr")))

print('senior el nino'.title()) # prints Senior El Nino
print('Super'.islower()) # prints false
print('Veramente bello, complimenti, molto bello!'.count('bello')) # 2
print('Very {} stuff can be made with {}.'.format('bad', 'intent'))

print('armadillo'.isalnum())
print('codey'.isprintable())
print('super is very super'.find('super'))
print('super is very super'.rfind('super'))
print('super is very super'.count('super'))