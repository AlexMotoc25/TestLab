sir ="""Dacă nimic neprevăzut nu se va întâmpla, România va evita să dea piept cu adversari ca Ucraina, Turcia, Polonia, Ungaria, Serbia și Norvegia. 
Astfel, România are nevoie de un succes sau de două remize din meciurile cu Kosovo și Cipru, pentru a fi sigură de prezența în urna a doua."""

nr_char_prima_parte = len(sir) // 2
prima_parte= sir[: nr_char_prima_parte].upper().strip()

parte_doi = sir[nr_char_prima_parte].capitalize()
print(prima_parte, parte_doi)
