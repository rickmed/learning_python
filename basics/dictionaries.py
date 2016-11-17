person = {
    'name': 'ricky',
    'lastN': 'medina',
    'age': 3
}

print(person['name'], person['age'])
print('Hello %(name)s. You have %(age)d years old' %person)


print('height' in person) # check for key existance
print('age' in person)
