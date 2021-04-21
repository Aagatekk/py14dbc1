# Here the blueprint for a wizard will be stored
class Wizard:

    def __init__(self, name, age,
                 school, is_a_good_student, fought_lord_voldemort,
                 friends, eye_colour, position_in_quiddich, superpowers, wallet):
        self.name = name
        self.age = age
        self.school = school
        self.is_a_good_student = is_a_good_student
        self.fought_lord_voldemort = fought_lord_voldemort
        self.friends = friends
        self.eye_colour = eye_colour
        self.position_in_quiddich = position_in_quiddich
        self.superpowers = superpowers.copy()
        self.waller = wallet

    def display_basics(self):
        return '{} {} {}'.format(self.name, self.age, self.is_a_good_student)


superpowers = {'flying': 51, 'casting spells': 100, 'talking to snakes': 10,
               'surviving lord voldermort\'s attacks': 10000}
wallet = {'USD': 170, 'GBP': 100, 'EUR': 200}
harry = Wizard('Harry', 13, 'Hogwarts', None, True, ['Ron', 'Hermione'], 'green', 'seeker', superpowers, wallet)
hermione = Wizard('Hermione', 13.5, 'Hogwarts', True, False, ['Harry', 'Ron'], 'brown', None, superpowers, wallet)
ron = Wizard('Ron', 13, 'Hogwarts', False, False, ['Harry', 'Hermione'], 'brown', 'keeper', superpowers, wallet)
victor = Wizard('Victor', 16, 'Durmstrang', None, False, [None], 'brown', 'seeker', superpowers, wallet)

print(superpowers.keys())
print(wallet)

while True:
    chosen_superpower = input('\nPlease type a superpower from the list to see how useful it is\n')
    if chosen_superpower in superpowers:
        if 50 < superpowers.get(chosen_superpower) < 60:
            print('Cool')
        elif superpowers.get(chosen_superpower)>60:
            print('Supercool')
        else:
            print('Still a superpower')
        break
    else:
        print('Please choose an existing superpower')




#while True:
#    user_added_superpower = input("\nEnter superpower:\n")
#    superpower_power = input('enter the power of the superpower between 1 and a 100')

#    if user_added_superpower in superpowers:
#        print(user_added_superpower + ' already on the list ')
#        print(superpowers)
#        print(' See?. Please add a different superpower')
#        if superpower_power > 100 or superpower_power < 1:
#            print('Please provide a number between 1 and a 100')
#    else:
#        superpowers.update({user_added_superpower: superpower_power})
#        print('superpower added ')
#        print(superpowers)
#        break

