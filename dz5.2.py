import itertools

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

def tuturs_klasses(tutors, klasses):

    tuturs_klasses1 = (f'({name}, {klass})' for name, klass in itertools.zip_longest(tutors, klasses))
    yield tuturs_klasses1

name_klass = next(tuturs_klasses(tutors, klasses))
# for a in name_klass:
#     print(a)
print(next(name_klass))
print(next(name_klass))
print(next(name_klass))
print(next(name_klass))
print(next(name_klass))
print(next(name_klass))
print(next(name_klass))
print(next(name_klass))

# print(*(tuturs_klasses(tutors, klasses)))

