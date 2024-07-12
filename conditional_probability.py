#simulating the typical example of a family with two kids either boy or girl.
#checking conditional probability for both girls 1.) if the older kid is a girl.
#                                                2.) if atleast one child is a girl.

import random
def random_kid():
    return random.choice(['boy', 'girl'])

random.seed(0)#to generate random numbers.

both_girl = 0
either_girl = 0
older_girl = 0

for i in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == 'girl' and younger == 'girl':
        both_girl += 1
    if older == 'girl' or younger == 'girl':
        either_girl += 1
    if older == 'girl':
        older_girl += 1
        
print(f'P(Both| older) = {both_girl / older_girl}') #approximately 1/2 as given by theory also.
print(f'P(Both| either) = {both_girl / either_girl}') #approximately 1/3 as given by theory also.
