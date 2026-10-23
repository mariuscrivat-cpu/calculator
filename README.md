# calculator

Mic proiect Python: funcții de calcul (`calculator.py`) și o interfață web de tip calculator servită cu [Eel](https://github.com/python-eel/Eel).

## Funcții existente (`calculator.py`)
- `adunare(a, b)` (add), `scadere(a, b)` (subtract), `multiply(a, b)`, `divide(a, b)` (ridică `ZeroDivisionError` la împărțire la zero), `putere(a, b)`.

> UI-ul este un calculator funcțional în browser (evaluare cu math.js).

## Structura proiectului
- `calculator.py` – logica de calcul
- `config.py` – citirea configurației (HOST/PORT)
- `app.py` – punctul de intrare (server Eel)
- `web/` – `index.html` (Bootstrap + Alpine.js + math.js via CDN, fără CSS/JS propriu)
- `tests/` – teste
- `Makefile` – target-uri `start`, `install`, `test`
- `.env.local`, `.env.example` – variabile de mediu
- `requirements.txt`, `verify.sh`

## Cerințe
Python 3.8+ și pachetele din `requirements.txt` (Eel, python-dotenv).

## Instalare
```
make install   # creează .venv și instalează dependențele
```

## Rulare
```
make start
```
Aplicația pornește pe http://127.0.0.1:8080 (deschide adresa în browser).

## Teste
```
make test      # sau: bash verify.sh
```

## Variabile de mediu
Se citesc din mediu sau din `.env.local` (copiază `.env.example`; fișierul este ignorat de git).

| Variabilă | Implicit |
|-----------|----------|
| `HOST` | `127.0.0.1` |
| `PORT` | `8080` |
