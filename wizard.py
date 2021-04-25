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
    return cool_superpowers


# coolness_value = int(input('Please provide superpower coolness value\n'))
# print(find_cool_superpowers(superpowers, coolness_value))


def shopping(amount, cost):
    new_amount = amount - cost
    return new_amount


# currency = input("Please provide currency abbreviation\n").upper()
# cost = int(input("Please provide the cost of the item you ant to buy\n"))

# if currency in wallet.keys():
# if (wallet[currency] - cost) >= 0:
# wallet[currency] = shopping(wallet[currency], cost)
# print('You spent ' + str(cost) + ". and have left")
# print(wallet.items())
# else:
# print("Sorry, you're broke")
# else:
# print("You don't have this currency")


# def reverse(text):
# return text[::-1]


# for n in range(99, 0, -1):
#   print(n, "bottles of rum on the wall")

# squares = [x * x for x in range(1, 5001)] # list comprehension
# print(squares)


a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# iterate over the old list taking each element and squaring it create a new list from those squares, then sum() it
def sum_of_squares_function(list):
    sum_of_squares = sum([x * x for x in a_list])
    return sum_of_squares


# print(sum_of_squares_function(a_list)) #second argument even if not specified is always 0, so sum of None is 0.

nums = [1, 7, 11, 8]
target = 9


def indices_of_a_given_sum(nums, target):
    new_list = []
    for i in range(len(nums)):
        second_substrate = target - nums[i]
        if second_substrate in nums:
            new_list.append(nums.index(nums[i]))
            new_list.append(nums.index(second_substrate))
            break
        else:
            continue
    return new_list


print(indices_of_a_given_sum(nums, target))
