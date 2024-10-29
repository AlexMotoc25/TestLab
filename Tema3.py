meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

while studenti:
    
    comanda = comenzi.pop()
    student1 = studenti.pop()
    
    tavi.pop()
    istoric_comenzi.append(comanda)
    
    cata_ceafa_exista = meniu.count("ceafa") - istoric_comenzi.count("ceafa")
    cat_guias_exisa = meniu.count("guias") - istoric_comenzi.count("guias")
    cati_papanasi_exista = meniu.count("papanasi") - istoric_comenzi.count("papanasi")    
    
    print(f"{student1} a comandat {comanda}")
        
if cata_ceafa_exista > 0:
    print(f"Au mai ramas{cata_ceafa_exista} portii de ceafa")
else:
    print("Nu a mai ramas ceafa")
    
if cat_guias_exisa > 0:
    print(f"Au mai ramas {cat_guias_exisa} portii de guias")
else:
    print("nu mai exista guias")
    
if cati_papanasi_exista > 0:
    print(f"Au mai ramas {cati_papanasi_exista} portii de papanasi")
else:
    print("nu mai exista papanasi")
    
print(f"Mai sunt {len(tavi)} tavi")
print(f"S-au comandat {istoric_comenzi.count("ceafa")} cefe, {istoric_comenzi.count("guias")} guias si {istoric_comenzi.count("papanasi")} papanasi")

def bani_facuti():
    bani_papanasi = preturi[0][1] * istoric_comenzi.count("papanasi")
    bani_ceafa = preturi[1][1] * istoric_comenzi.count("ceafa")
    bani_guias = preturi[2][1] * istoric_comenzi.count("guias")
    print(f"Cantina a incasat {bani_papanasi + bani_ceafa + bani_guias} lei")

def cost():
    for produs in preturi:
        pret = produs[1]
        
        if pret <= 7:
            print(f"Produse care costă cel mult 7 lei: {produs[0]}")
        
bani_facuti()
cost()