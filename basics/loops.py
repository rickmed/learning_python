# for i in range(5):
#     print(i)
#
# for x in range(3, 7):
#     print(x, '', end='')  # end means no new lines
#
# list1 = ['item1', 'item2', 'item3']
#
# for i in list1:
#     print(i)

import random

random_num = random.randrange(10, 20)

while(random_num != 15):
    if (random_num == 13):
        print('Reached', random_num, '. Stopping...')
        break
    else:
        print(random_num)
        random_num = random.randrange(10, 20)
        continue
