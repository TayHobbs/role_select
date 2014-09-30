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
