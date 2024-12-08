import math

def cauta_container(containere, numar_identificare):
    n = len(containere)
    salt = int(math.sqrt(n))
    numar_pasi = 0  
    st = 0  
    
    for i in range(0, n, salt):
        numar_pasi += 1  
        if containere[i] == numar_identificare:
            print(f"Containerul cu numărul {numar_identificare} a fost găsit pe poziția {i} după {numar_pasi} pași.")
            return i
        elif containere[i] > numar_identificare:
            break
        st = i  

    
    for i in range(st, min(st + salt, n)):
        numar_pasi += 1  
        if containere[i] == numar_identificare:
            print(f"Containerul cu numărul {numar_identificare} a fost găsit după {numar_pasi} pași.")
            return i  
    
   
    print(f"Containerul cu numărul {numar_identificare} nu a fost găsit în sistem. Total pași efectuați: {numar_pasi}.")
    return -1  
cauta_container([1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080], 1030)