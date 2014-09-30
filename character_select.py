from roles import Role, Warrior, Hunter, Rouge, Priest, Familiar


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

    
def custom_select():
    choice = raw_input("What class would you like to play? (Warrior, Priest, Rouge, Hunter) => ")
    if choice.lower() == 'warrior':
        role = Warrior()
    elif choice.lower() == 'priest':
        role = Priest()
    elif choice.lower() == 'rouge':
        role = Rouge()
    elif choice.lower() == 'hunter':
        role = Hunter()
    else:
        role = custom_select()
    return role

def ask_question(questions):
    number = 0
    for q in questions:
        answer = raw_input(q)
        if answer.lower() == 'y':
            number += 1

    return number


def suggest_role(num):
    if num <= 3:
        choice = raw_input("Your suggested role is a Priest, and your partner would be a Rouge. Are you happy with this choice? (y/n) =>")
        if choice.lower() == 'y':
            role = Priest()
            return role
        else:
            custom_select()
    elif num <= 5:
        choice = raw_input("Your suggested role is a Rouge, and your partner would be a Priest. Are you happy with this choice? (y/n) =>")
        if choice.lower() == 'y':
            role = Rouge()
            return role
        else:
            custom_select()
    elif num <=7:
        choice = raw_input("Your suggested role is a Hunter, and your familiar would be a Panther. Are you happy with this choice? (y/n) =>")
        if choice.lower() == 'y':
            role = Hunter()
            return role
        else:
            custom_select()
    else:
        choice = raw_input("Your suggested role is a Warrior, and your familiar would be a Priest. Are you happy with this choice? (y/n) =>")
        if choice.lower() == 'y':
            role = Warrior()
            return role
        else:
            role = custom_select()
            return role
            
number = ask_question(questions)
role = suggest_role(number)

print "Your name is {}, you are a {} and use a {}".format(role.name, role.job, role.weapon)
# print "Your party member's name is {}, a {}".format(partner.name, partner.job)
