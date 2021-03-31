### f strings
def get_name_and_decades(name, age):
    return f"My name is {name} and I'm {age / 10:.5f} decades old."

print(get_name_and_decades("Maria", 31))
#My name is Maria and I'm 3.10000 decades old.

print(">"*20)
###remember sorted for array
###check for anagrams
x = 'abcd'
y = 'dcab'

lista = list(x)
listb = list(y)

lista = sorted(lista)
listb = sorted(listb)

if lista == listb:
    print('They are anagrams')
print(">"*20)
import random
all_words = "Doyin, your love they high me like igboli".split()
def get_random_word():
    return random.choice(all_words)
def get_unique_words():
    words = set()
    for _ in range(1000):
        words.add(get_random_word())
    return words
print(get_unique_words())

cowboy = {'age': 32, 'horse': 'mustang', 'hat_size': 'large'}
if 'name' in cowboy:
    name = cowboy['name']
else:
    name = 'The Man with No Name'

print(name)
def mrEazi():
    print('you gotta show me')
konami = cowboy.get('Name','Doyin')
print(konami)
cowboy.get('Name',mrEazi())
print('>'*20)
student_grades = {}
grades = [
('elliot', 91),
('neelam', 98),
('bianca', 81),
('elliot', 88)]
for name, grade in grades:
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(grade)
print(student_grades)


# >>> import string
# >>> def is_upper(word):
# ...     for letter in word:
# ...         if letter not in string.ascii_uppercase:
# ...             return False
# ...     return True
# ...
# >>> is_upper('Thanks Geir')
# False
# >>> is_upper('LOL')
# True 

print('>'*20)
name = 'DoNyI'

for x in name:
    if x.isupper():
        print(x)

#   class Pet(object):
#     num_pets = 0
#     def __init__(self, name):
#         self.name = name

#         # change from: self.num_pets += 1
#         Pet.num_pets += 1
#       def speak(self):
#         print("My name's %s and the number of pets is %d" % (self.name, self.num_pets))   

print('>'*20)

# iterator = (i for i in range(1, 4))
# matrix = [[x * y for y in iterator] for x in iterator]

# iterator = [i for i in range(1, 4)]
# matrix = [[x * y for y in iterator] for x in iterator]