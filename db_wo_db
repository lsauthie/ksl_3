def menue_anzeigen():
    print("\n=== EINKAUFSLISTE ===")
    print("1. Einen Artikel hinzufügen")
    print("2. Liste anzeigen")
    print("3. Einen Artikel löschen")
    print("4. Beenden")

def artikel_hinzufuegen(liste):
    artikel = input("Geben Sie den Namen des Artikels ein, den Sie hinzufügen möchten: ")
    liste.append(artikel)
    print(f"✔ '{artikel}' wurde zur Liste hinzugefügt.")

def liste_anzeigen(liste):
    if not liste:
        print("Die Liste ist leer.")
    else:
        print("\nIhre Einkaufsliste:")
        for i, item in enumerate(liste, 1):
            print(f"{i}. {item}")

def artikel_loeschen(liste):
    liste_anzeigen(liste)
    if liste:
        try:
            index = int(input("Nummer des zu löschenden Artikels: "))
            artikel = liste.pop(index - 1)
            print(f"🗑 '{artikel}' wurde gelöscht.")
        except:
            print("Ungültige Eingabe.")

def main():
    einkaufsliste = []
    while True:
        menue_anzeigen()
        wahl = input("Bitte wählen Sie eine Option: ")

        if wahl == "1":
            artikel_hinzufuegen(einkaufsliste)
        elif wahl == "2":
            liste_anzeigen(einkaufsliste)
        elif wahl == "3":
            artikel_loeschen(einkaufsliste)
        elif wahl == "4":
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Auswahl.")

main()
