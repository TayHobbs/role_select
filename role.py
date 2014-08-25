class Role(object):

    def __init__(self, health, name, job, weapon, title, magic):
        self.health = health
        self.name = name
        self.job = job
        self.weapon = weapon
        self.title = title
        self.magic = magic

class Warrior(Role):
    attack = 'Sheild Slam'

    def __init__(self):
        super(Warrior, self).__init__(
                200,
                'Brothgar',
                'Warrior',
                'shield',
                'The Brave',
                50)


class Priest(Role):
    spell = 'Heal'

    def __init__(self):
        super(Priest, self).__init__(
                100,
                'Alinia',
                'Priest',
                'staff',
                'The Healing',
                200)

class Rouge(Role):
    attack = 'Strike'

    def __init__(self):
        super(Rouge, self).__init__(
                150,
                'Granzine',
                'Rouge',
                'daggers',
                'The Quick',
                30)

class Hunter(Role):
    attack = 'Deathblow'

    def __init__(self):
        super(Hunter, self).__init__(
                125,
                'Callamine',
                'Hunter',
                'bow',
                'The Swift',
                100)

class Familiar(Role):
    attack = 'Swipe'
    animal = 'panther'


    def __init__(self):
        super(Familiar, self).__init__(
                200,
                'Gwen',
                'Familiar',
                'claws',
                'The Loyal',
                25)


questions = [
    ("Do you like protecting your friends? (y/n) => "),
    ("Do you like being a leader? (y/n) => "),
    ("Do you like being in the background? (y/n) => "),
    ('Do you like dealing damage up close? (y/n) => '),
    ('Far away? (y/n) => '),
    ("Do you like working alone? (y/n) => "),
    ('Do you like melee? (y/n) => '),
    ('Ranged? (y/n) => ')
]

    
def ask_question(questions):
    number = 0
    for q in questions:
        answer = raw_input(q)
        if answer.lower() == 'y':
            number += 1

    return number

number = ask_question(questions)

if number <= 3:
    role = Priest()
    partner = Rouge()
elif number <= 5:
    role = Rouge()
    partner = Priest()
elif number <=7:
    role = Hunter()
    partner = Familiar()
else:
    role = Warrior()
    partner = Priest()


print "Your name is %s, you are a %s and use a %s" % (role.name, role.job, role.weapon)
print "Your party member's name is %s, a %s" %  (partner.name, partner.job)
