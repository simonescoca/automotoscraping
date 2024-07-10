import os
import json

def main():
    file = input("> inserisci il JSON da ordinare in formato nome-file.json: ")

    if os.path.exists(f"{os.getcwd()}/{file}"):
        key1 = input(f"> scegli la prima key su cui basare l'ordine di {file}: ")
        key2 = input(f"> scegli la seconda key su cui basare l'ordine di {file} (lascia vuoto per bypassare): ")

        # Carica il file JSON
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        try:
            if key2:
                # Ordina i dati in base alle chiavi key1 e key2
                data_sorted = sorted(data, key=lambda x: (x[key1].lower(), x[key2].lower()))
            else:
                # Ordina i dati solo in base alla chiave key1
                data_sorted = sorted(data, key=lambda x: x[key1].lower())
        except KeyError as e:
            print(f"> la key {e} non è valida 𝘹")
            return

        # Salva i dati ordinati di nuovo nel file JSON
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data_sorted, f, ensure_ascii=False, indent=4)

        print(f"> {file} ordinato e salvato ✔")
    else:
        print(f"> {file} non esiste 𝘹")

if __name__ == "__main__":
    main()