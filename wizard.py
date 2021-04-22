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


superpowers = {'flying': 60, 'casting spells': 80, 'talking to snakes': 10,
               "surviving lord voldermort\'s attacks": 100}  # using double quotes doesn't require using escape characters
wallet = {'USD': 170, 'GBP': 100, 'EUR': 200}
harry = Wizard('Harry', 13, 'Hogwarts', None, True, ['Ron', 'Hermione'], 'green', 'seeker', superpowers, wallet)
hermione = Wizard('Hermione', 13.5, 'Hogwarts', True, False, ['Harry', 'Ron'], 'brown', None, superpowers, wallet)
ron = Wizard('Ron', 13, 'Hogwarts', False, False, ['Harry', 'Hermione'], 'brown', 'keeper', superpowers, wallet)
victor = Wizard('Victor', 16, 'Durmstrang', None, False, [None], 'brown', 'seeker', superpowers, wallet)


def find_cool_superpowers(superpowers, coolness_value):
    cool_superpowers = []

    for key, value in superpowers.items():
        if int(superpowers[key]) > coolness_value:
            cool_superpowers.append(key)
    print(cool_superpowers)


coolness_value = int(input('please provide superpower coolness value\n'))
find_cool_superpowers(superpowers, coolness_value)


def shopping(wallet, currency, cost):
    # pull currency amount from the wallet
    if currency in wallet.keys():
        if (wallet[currency] - cost) >= 0:
            wallet[currency] = wallet[currency] - cost
            print('You spent ' + str(cost))
        else:
            print("Sorry, you're broke")
    else:
        print("You don't have this currency")


currency = input("Please provide currency abbreviation\n").upper()
cost = int(input("Please provide the cost of the item you ant to buy\n"))
shopping(wallet, currency, cost)