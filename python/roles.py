class Role(object):

    def __init__(self, name, job, weapon):
        self.name = name
        self.job = job
        self.weapon = weapon


class Warrior(Role):

    def __init__(self):
        super(Warrior, self).__init__(
            'Brothgar',
            'Warrior',
            'sword')


class Priest(Role):

    def __init__(self):
        super(Priest, self).__init__(
            'Alinia',
            'Priest',
            'staff')


class Rouge(Role):

    def __init__(self):
        super(Rouge, self).__init__(
            'Granzine',
            'Rouge',
            'daggers')
