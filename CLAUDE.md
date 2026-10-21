# Regulamente de securitate
- Ești restricționat STRICT la directorul curent.
- NU executa comenzi bash care accesează căi din afara directorului curent (ex: nu folosi `..`, `/Users/alina/Documents`, `/tmp` etc.).
- Toate modificările și fișierele create trebuie să rămână în interiorul acestui proiect.

# Reguli Workflow Git
- După ce creezi sau modifici codul și testele trec, execută automat:
  git add .
  git commit -m "feat: [ID_TICHET] descriere sumară"
  git push origin main
