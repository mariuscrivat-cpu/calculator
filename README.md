# calculator

Mic proiect Python care conține funcții de calcul aritmetic (`calculator.py`) și o interfață web de tip calculator, servită local cu [Eel](https://github.com/python-eel/Eel). Serverul își ia configurația (host, port) din variabile de mediu sau din `.env.local`.

## Structura proiectului
```
.
├── calculator.py      # funcțiile de calcul
├── config.py          # citirea configurației (HOST/PORT)
├── app.py             # punctul de intrare: pornește serverul web Eel
├── web/
│   └── index.html     # UI-ul calculatorului
├── tests/             # testele (unittest)
│   ├── test_app.py
│   ├── test_calculator.py
│   ├── test_config.py
│   ├── test_makefile.py
│   └── test_ui.py
├── Makefile           # target-uri install / start / test
├── requirements.txt   # dependențe Python
├── verify.sh          # rulează testele în formatul cerut de orchestrator
├── pytest.ini         # setări pentru rulare cu pytest (opțional)
├── .env.example       # model de configurare
└── .env.local         # configurare locală (ignorat de git)
```

## Funcțiile calculatorului (`calculator.py`)
| Funcție | Descriere |
|---------|-----------|
| `adunare(a, b)` | `a + b` |
| `scadere(a, b)` | `a - b` |
| `multiply(a, b)` | `a * b` |
| `divide(a, b)` | `a / b`; ridică `ZeroDivisionError` dacă `b == 0` |
| `putere(a, b)` | `a ** b` (a la puterea b) |

## Serverul web și UI-ul
`app.py` inițializează Eel pe directorul `web/` și pornește serverul cu `host` și `port` din configurație (`mode=False`: nu se deschide automat o fereastră de browser). Implicit adresa este http://127.0.0.1:8080 — deschide-o manual în browser.

UI-ul (`web/index.html`) este un calculator funcțional cu taste pentru cifre, `+ − × ÷`, `.`, `=` și `C` (resetare). Expresiile sunt evaluate în browser cu math.js; erorile de evaluare afișează `Eroare`. Pagina nu are CSS/JS propriu în fișiere separate: folosește, încărcate prin CDN (jsDelivr), [Bootstrap](https://getbootstrap.com) 5.3 (stil), [Alpine.js](https://alpinejs.dev) 3 (interactivitate) și [math.js](https://mathjs.org) 13 (evaluare), plus `/eel.js` servit de Eel. Este nevoie deci de conexiune la internet pentru a încărca aceste resurse.

## Configurare (`.env.local`)
Configurația se citește cu librăria [python-dotenv](https://pypi.org/project/python-dotenv/) (`dotenv_values`) din `.env.local`. Copiază modelul și editează-l:
```
cp .env.example .env.local
```
| Variabilă | Implicit | Descriere |
|-----------|----------|-----------|
| `HOST` | `127.0.0.1` | adresa pe care ascultă serverul |
| `PORT` | `8080` | portul serverului |

Prioritate: variabilele de mediu reale, apoi `.env.local`, apoi valorile implicite. `.env.local` este ignorat de git.

## Dependențe
Python 3.8+ și pachetele din `requirements.txt`:
- `eel` – server web și legătura Python–browser
- `python-dotenv` – citirea `.env.local`

Testele folosesc doar `unittest` din biblioteca standard.

## Utilizare cu Makefile
```
make install   # creează .venv și instalează dependențele din requirements.txt
make start     # (rulează install dacă e nevoie) pornește serverul pe HOST:PORT, implicit http://127.0.0.1:8080
make test      # (rulează install dacă e nevoie) rulează testele din tests/
```
Se poate alege alt interpretor: `make install PYTHON=python3.12`.

## Teste
Toate testele se află în directorul `tests/`. Rulare:
```
make test                                   # în .venv, unittest discover -s tests -t .
bash verify.sh                              # python3 -m unittest discover; afișează liniile TEST: și TESTS_COUNT=<n>
python3 -m unittest discover -v -s tests -t .
```
`verify.sh` folosește `python3` din sistem, deci `eel` și `python-dotenv` trebuie să fie instalate și acolo (sau rulează scriptul cu `.venv` activat).
