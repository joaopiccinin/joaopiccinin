from time import sleep
from emoji import emojize
print('Os fogos vão explodir em...')
for c in range(10, 0, -1):
    sleep(1)
    print('{}...'.format(c))
print(emojize('BUUMMM :collision: '))