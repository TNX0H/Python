from itertools import count

for el in count(7):
    if el > 15:
        break
    else:
        print(el)

from itertools import cycle

с = 0
for el in cycle("ABC"):
    if с > 10:
        break
    print(el)
    с += 1