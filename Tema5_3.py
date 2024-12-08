numar_iteratii = 0

def cautare_binara(arr, start, stop, val):
    global numar_iteratii
    # Binary search with step counting
    while start <= stop:
        numar_iteratii += 1  # Count the iteration
        mij = start + (stop - start) // 2
        if arr[mij] == val:
            return mij
        elif val > arr[mij]:
            start = mij + 1
        else:
            stop = mij - 1
    return -1

def cauta_pacient(pacienti, id_pacient):
    global numar_iteratii
    n = len(pacienti)
    pasi = 0  # Count steps in exponential search
    if pacienti[0] == id_pacient:
        print(f"Dosarul pacientului cu numărul de identificare {id_pacient} a fost găsit la poziția 0 după 1 pas de căutare.")
        return 0
    
    i = 1
    while i < n and pacienti[i] < id_pacient:
        pasi += 1  # Increment steps only for valid comparisons
        i *= 2  # Double the range
    
    # Perform binary search in the narrowed range
    start = i // 2
    stop = min(i, n - 1)
    rezultat = cautare_binara(pacienti, start, stop, id_pacient)
    
    total_pasi = pasi + numar_iteratii
    if rezultat != -1:
        print(f"Dosarul pacientului cu numărul de identificare {id_pacient} a fost găsit la poziția {rezultat} după {total_pasi} pași de căutare.")
    else:
        print(f"Dosarul pacientului cu numărul de identificare {id_pacient} nu a fost găsit. Total pași efectuați: {total_pasi}.")
    
    return rezultat
	
cauta_pacient(range(1, 1000000, 7), 7778)
