import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]
incercari_ramase = 6
litere_incercate = []

while "_" in progres:
    print("".join(progres))
    l = input("").lower()
    litere_incercate.append(l)
    print(f'ai incercat {litere_incercate}')
        
    if l in cuvant_de_ghicit:
        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == l:
                progres[i]= l
                
    else:
        incercari_ramase -= 1
        print('litera gresita')
        print(f'mai ai {incercari_ramase} incercari')
        if incercari_ramase == 0:
            print(f"Ai pierdut, cuvantul era:{cuvant_de_ghicit}")
            break