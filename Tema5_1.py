def cauta_document(tab, numar_referinta):
    n = len(tab)
    pozitie = -1
    numar_iteratii = 0
    for i in range(n):
        numar_iteratii += 1
        pozitie += 1
        if tab[i] == numar_referinta: 
            print(f"Documentul cu numărul de referință {numar_referinta} a fost găsit pe poziția {pozitie} după {numar_iteratii} documente verificate.")
            break
    else:
        print(f"Documentul cu numărul de referință {numar_referinta} nu a fost găsit în dosar. Total documente verificate: {numar_iteratii}.")