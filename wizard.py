# Here the blueprint for a wizard will be stored
class Wizard:

    def __init__(self, name, age,
                 school, is_a_good_student, fought_lord_voldemort,
                 friends, eye_colour, position_in_quiddich, superpowers):
        self.name = name
        self.age = age
        self.school = school
        self.is_a_good_student = is_a_good_student
        self.fought_lord_voldemort = fought_lord_voldemort
        self.friends = friends
        self.eye_colour = eye_colour
        self.position_in_quiddich = position_in_quiddich
        self.superpowers = superpowers

    def display_basics(self):
        return '{} {} {}'.format(self.name, self.age, self.is_a_good_student)


superpowers = list(('flying', 'casting spells', 'talking to snakes', 'surviving lord voldermort\'s attacks'))

harry = Wizard('Harry', 13, 'Hogwarts', None, True, ['Ron', 'Hermione'], 'green', 'seeker', superpowers)
hermione = Wizard('Hermione', 13.5, 'Hogwarts', True, False, ['Harry', 'Ron'], 'brown', None, superpowers)
ron = Wizard('Ron', 13, 'Hogwarts', False, False, ['Harry', 'Hermione'], 'brown', 'keeper', superpowers)
victor = Wizard('Victor', 16, 'Durmstrang', None, False, [None], 'brown', 'seeker', superpowers)

# print(type(harry))
# print(harry.name, harry.friends, harry.is_a_good_student)
# print(hermione.display_basics())
# print(harry.__dict__)
# print(victor.display_basics())

# print(str(hermione.name[7:8]) + str(hermione.name[6:7]) + str(hermione.name[5:6]) + str(hermione.name[4:5]) + str(
#    hermione.name[3:4]) + str(hermione.name[2:3]) + str(hermione.name[1:2]) + str(hermione.name[0:1]))

# for letter in hermione.name[::-1]:
#    print(letter, end='')

# hn = list(hermione.name)
# hn.reverse()
# print('\n', hn)

print(superpowers)

while 1 == 1:
    user_added_superpower = input("\nEnter superpower:\n")

    if user_added_superpower in superpowers:
        print(user_added_superpower + ' already on the list ')
        print(superpowers)
        print(' See?. Please add a different superpower')
        continue
    else:
        superpowers.append(user_added_superpower)
        print('superpower added ')
        print(superpowers)
        break
