import operator

print "What class is best for you?"

role = {'warrior': 0, 'priest': 0, 'rouge': 0, 'hunter': 0};

print "Do you like protecting your friends?"
prot = raw_input()
if prot == 'yes' or prot == 'Yes':
   role['warrior'] += 1
   role['priest'] += 2
elif prot == 'no' or prot == 'No':
    role['rouge'] += 1
else:
    print "Fine, don't answer."
    role['hunter'] += 2

print "Do you like being a leader?"
lead = raw_input()
if lead == 'yes' or lead == 'Yes':
    role['warrior'] += 1
elif lead == 'no' or lead == 'No':
    role['hunter'] += 1
else:
    print "Fine, don't answer."

print "Do you like being in the background?"
back = raw_input()
if back == 'yes' or back == 'Yes':
    role['rouge'] += 1
    role['hunter'] += 2
elif back == 'no' or back == 'No':
    role['priest'] += 1
else:
    print "Fine, don't answer."

print "Do you like dealing damage up close?"
close = raw_input()
if close == 'yes' or close == 'Yes':
    role['rouge'] += 1
    role['warrior'] += 1
elif close == 'no' or close == 'No':
    role['hunter'] += 1
    role['priest'] += 1
else:
    print "Fine, don't answer."


print "Far away?"
distance = raw_input()
if distance == 'yes' or distance == 'Yes':
    role['hunter'] += 2
    role['priest'] += 1
elif distance == 'no' or distance == 'No':
    role['rouge'] += 1
    role['warrior'] += 1
else:
    print "Fine, don't answer."

print "Do you like working alone?"
alone = raw_input()
if alone == 'yes' or alone == 'Yes':
    role['rouge'] += 2
    role['hunter'] += 1
    role['warrior'] -= 1
elif alone == 'no' or alone == 'No':
    role['priest'] += 2
else:
    print "Fine, don't answer."
    
print "Do you like wearing heavy, medium or light armor?"
armor = raw_input()
if armor == 'heavy' or armor == 'Heavy':
    role['warrior'] += 3
elif armor == 'medium' or armor == 'Medium':
    role['rouge'] += 3
    role['hunter'] += 3
else:
    role['priest'] += 3

print "Do you like swords, magic or bows?"
weapon = raw_input()
if weapon == 'swords' or weapon == 'Swords' or weapon == 'sword' or weapon == 'Sword':
    role['warrior'] += 2
    role['rouge'] += 2
elif weapon == 'magic' or weapon == 'Magic':
    role['priest'] += 2
else:
    role['hunter'] += 2

# Going to implement later
#print "What is your favorite color?"
#color = raw_input()

character =  max(role.iteritems(), key=operator.itemgetter(1))[0]

print "Your class is " + character

print "What would you like to name your class?"
name = raw_input()

print "\n" +  name.capitalize() + " the " + character

#print role['warrior']
#print role['rouge']
#print role['priest']
#print role['hunter']
#titles for all the roles to be added later The Brave/swift/quick/healing
