import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]
incercari_ramase = 6
litere_incercate = []


while "_" in progres:
    print("".join(progres))
    l = input("Introdu o litera:").lower()
    
    if not l.isalpha() or len(l) != 1:
        print("Te rog sa introduci doar o litera.")
        continue
    
    if l in litere_incercate:
        print("Ai incercat deja aceasta litera")
        continue
    
    litere_incercate.append(l)
    
    if l in cuvant_de_ghicit:
        print(f'Ai incercat {litere_incercate}')
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == l:
                progres[i]= l
    else:
        incercari_ramase -= 1
        print('Litera gresita')
        print(f'Ai incercat {litere_incercate}')
        print(f'Mai ai {incercari_ramase} incercari')
        if incercari_ramase == 0:
            print(f"Ai pierdut! Cuvântul era:{cuvant_de_ghicit}")
            break
        
    if "_" not in progres:
        print(f"Felicitări! Ai ghicit cuvântul:{cuvant_de_ghicit}")
        break