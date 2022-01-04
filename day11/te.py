lista=[{"a":"s","b":2},{"a":"w","b":2},{"a":7,"b":2}]

def s(qq):
    for i in range(len(lista)):
        if 7 == lista[i][qq]:
            print(1)

from User import User
for i in range(5):
    jack=User(1,1,1,1)
    print(jack.getAccountNumber())