#https://www.pythontutorial.net/python-basics/python-write-text-file/
"""
f = open('C:/Users/monic/OneDrive/Dokumente/KI_Data/GeoPy/python/python/addresses.txt.txt')
f
for line in f:
    print(line)

o = open('C://Users//monic//OneDrive//Dokumente//KI_Data//GeoPy//python//python//addout.csv', 'w')

for line in f:
    o.write(line)
o.close
"""

with open('readme.txt', 'w') as f:
    f.write('readme')

lines = ['Readme', 'How to write text files in Python']
with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

a = open('addresses.txt.txt') #documento ya estaba
f = open('readme.txt', 'w')

for line in a:
    f.write(line)
f.close

a = open('addresses.txt.txt')
c = open('googleoutaddress.csv', 'w')
for line in a:
    c.write(line)
c.close