meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

cata_ceafa_exista = comenzi.count("ceafa")
cat_guias_exisa = comenzi.count("guias")
cati_papanasi_exista = comenzi.count("papanasi")

while studenti:
    for student in (studenti):
        student1 = studenti.pop()
        
    for comanda in (comenzi):
        comanda1 = comenzi.pop()

print(f"{student} a comandat {comanda}" )




