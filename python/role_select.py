from roles import Warrior, Rouge, Priest


questions = [
    ("Do you like protecting your friends? (y/n) => "),
    ("Do you like being a leader? (y/n) => "),
    ("Do you like being in the background? (y/n) => "),
    ('Do you like dealing damage up close? (y/n) => '),
    ('Far away? (y/n) => '),
    ("Do you like working alone? (y/n) => "),
    ('Do you like melee? (y/n) => '),
    ('Ranged? (y/n) => '),
]


class RoleSelection(object):

    def _ask_questions(self, questions):
        number = 0
        for question in questions:
            answer = raw_input(question)
            if answer.lower() == 'y':
                number += 1
        return number

    def _select_new_role(self):
        choice = raw_input("What class would you like to play?\
            (Warrior, Priest, Rouge) => ")
        if choice.lower() == 'warrior':
            role = Warrior()
        elif choice.lower() == 'priest':
            role = Priest()
        elif choice.lower() == 'rouge':
            role = Rouge()
        else:
            role = self._select_new_role()
        return role

    def _set_role(self, role):
        choice = raw_input("Your suggested role is a {}.\
            Are you happy with this choice? (y/n) => ".format(role().job))
        if choice.lower() == 'y':
            selected_role = role()
            return selected_role
        else:
            selected_role = self._select_new_role()
            return selected_role

    def _suggest_role(self, number):
        if number <= 3:
            role = self._set_role(Priest)
        elif number <= 5:
            role = self._set_role(Rouge)
        else:
            role = self._set_role(Warrior)
        return role

    def find_your_role(self):
        number = self._ask_questions(questions)
        selected_role = self._suggest_role(number)
        print "Your name is {}, you are a {} and use a {}".format(
            selected_role.name, selected_role.job, selected_role.weapon)

RoleSelection().find_your_role()
