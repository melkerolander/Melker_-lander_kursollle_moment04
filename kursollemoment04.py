x = int(input("Ange rektangelns första sida"))
y = int(input("Ange rektangelns andra sida"))

area = x*y

print(f"sidorna på rektangeln är {x} och {y} vilket gör att arean är {area}")

if x == y:
    print(f"första sidan och andra sidan är lika långa vilket betyder att det är en kvadrat")

for i in range(1,11):
    vol = area*i
    print(f"när höjden är {i} så blir volymen {vol}")

'''
2
'''
rekinfo = []

while True:
    x = int(input("Ange rektangelns första sida"))
    y = int(input("Ange rektangelns andra sida"))

    area = x*y

    print(f"sidorna på rektangeln är {x} och {y} vilket gör att arean är {area}")

    if x == y:
        print(f"första sidan och andra sidan är lika långa vilket betyder att det är en kvadrat")

    if x == y:
        rekinfo.append(f"när sidorna på rektangeln är {x} och {y} blir arean {area}, eftersom båda sidorna är lika långa")
    else:
        rekinfo.append(f"när sidorna på rektangeln är {x} och {y} blir arean {area}")

    for i in range(1,11):
        vol = area*i
        print(f"när höjden är {i} så blir volymen {vol}")
    
    while True:
        tal = str(input("vill du köra en till beräkning"))
        if tal in ('ja', 'nej'):
            break
        print("felaktigt tal")
    if tal == 'j':
        continue
    else:
        break
print(*rekinfo, sep = "/n")
    

