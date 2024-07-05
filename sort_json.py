import os
import json


file = input("> inserisci il JSON da ordinare in formato nome-file.json: ")

if  os.path.exists(f"{os.getcwd()}/{file}"):
    key = input(f"> scegli la key su cui basare l'ordine di {file}: ")

    # Carica il file JSON
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    try:
        # Ordina i dati in base alla chiave 'name'
        data_sorted = sorted(data, key=lambda x: x[key].lower())
    except:
        print("> la key non è valida")

    # Salva i dati ordinati di nuovo nel file JSON
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data_sorted, f, ensure_ascii=False, indent=4)

    print(f"> {file} ordinato e salvato ✔")

else:
    print(f"> {file} non esiste")