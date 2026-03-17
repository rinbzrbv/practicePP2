'''enumerate()

What it does: adds an index to each element
'''

students = ["Arman", "Dina", "Ruslan"]
for i, student in enumerate(students):
    print(i, student)

letters = ['x', 'y', 'z']
print(list(enumerate(letters)))
# [(0, 'x'), (1, 'y'), (2, 'z')]


'''zip()

What it does: combines multiple iterables into tuples
'''

names = ["Arman", "Dina"]
grades = [88, 92]

zipped = list(zip(names, grades))
print(zipped)  # [('Arman', 88), ('Dina', 92)]

cities = ["Almaty", "Astana"]
temps = [25, 30]

zipped2 = list(zip(cities, temps))
print(zipped2)  # [('Almaty', 25), ('Astana', 30)]