from pymongo import MongoClient
from time import sleep

from pymongo.errors import PyMongoError


def datenbank_und_kollektion_erstellen_und_verbinden():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["warenkatalog"]
        print("Datenbank erfolgreich verbunden.")
        sleep(3)
        collection = db["warenkatalog"]
        print("Tabelle erfolgreich verbunden.")
        sleep(3)
        return collection
    except PyMongoError:
        print("Es ist ein Fehler bei der Verbindung mit der Datenbank aufgetreten!")
        sleep(5)
def tabelle_zeigen():
    try:
        collection = datenbank_und_kollektion_erstellen_und_verbinden()
        warenkatalog = collection.find()
        print("ID | Produktname | Artikelnummer | Nettopreis | Bestand")
        sleep(5)
        for produkt in warenkatalog:
            print(f"\n{produkt['_id']} | {produkt['produktname']} | {produkt['artikelnummer']} | {produkt['nettopreis']} | {produkt['stock']}")
            sleep(0.5)
    except PyMongoError:
        print(f"Fehler beim Anzeigen der Tabelle: {PyMongoError}")
        sleep(5)
def artikel_hinzufügen():
    try:
        collection = datenbank_und_kollektion_erstellen_und_verbinden()
        name = input("Bitte geben Sie den Namen des Artikels ein: ")
        nummer = input("Bitte geben Sie die Nummer des Artikels ein: ")
        preis = float(input("Bitte geben Sie den Nettopreis des Artikels ein: "))
        stock = 0
        nosql = {"produktname": name, "artikelnummer": nummer, "nettopreis": preis, "stock": stock}
        collection.insert_one(nosql)
        print("Eintrag erfolgreich hinzugefügt.")
    except PyMongoError():
        print(f"Fehler beim hinzufügen des Eintrags: {PyMongoError}")
        sleep(5)
def tabelle_aktualisieren():
    try:
        collection = datenbank_und_kollektion_erstellen_und_verbinden()
        while True:
            try:
                update = {}
                id = input("Bitte geben Sie die ID des Eintrags ein, der geändert werden soll: ")
                sleep(3)
                aktualisieren = input("Bitte geben Sie die Spalte ein, die geändert werden soll: ")
                sleep(3)
                if aktualisieren == "nettopreis":
                    wert = float(input("Bitte geben Sie den neuen Wert an: "))
                elif aktualisieren == "stock":
                    wert = int(input("Bitte geben Sie den neuen Wert an: "))
                else:
                    wert = input("Bitte geben Sie den neuen Wert an: ")
                sleep(3)
                update[aktualisieren] = float(wert)
                break
            except Exception:
                print("Ungültige Eingabe!")
                sleep(3)
        nosql = collection.update_one({"_id": id}, {"$set": update})
        if nosql.matched_count > 0:
            print("Eintrag erfolgreich geändert.")
        else:
            print("Eintrag existiert nicht.")
        sleep(3)
    except PyMongoError():
        print(f"Fehler beim aktualisieren des Eintrags: {PyMongoError}")
        sleep(5)
def artikel_löschen():
    try:
        collection = datenbank_und_kollektion_erstellen_und_verbinden()
        while True:
            try:
                id = input("Bitte geben Sie die ID des Eintrags ein, der gelöscht werden soll: ")
                sleep(3)
                break
            except Exception:
                print("Ungültige Eingabe!")
                sleep(5)
        nosql = collection.delete_one({"_id": id})
        if nosql.deleted_count > 0:
            print("Eintrag erfolgreich gelöscht.")
        else:
            print("Eintrag existiert nicht.")
        sleep(3)
    except PyMongoError():
        print(f"Fehler beim löschen des Eintrags: {PyMongoError}")
        sleep(5)
def programm_beenden():
    print("\nLetzter Stand der Tabelle:\n")
    sleep(5)
    tabelle_zeigen()
    sleep(5)
    print("Programm beendet.")
    exit(0)
def main():
    try:
        datenbank_und_kollektion_erstellen_und_verbinden()
        menü = ["1 -> Tabelle anzeigen", "2 -> Artikel hinzufügen", "3 -> Tabelle aktualisieren",
                "4 -> Artikel löschen", "5 -> Programm beenden"]
        #print("Die Tabelle enthält noch keine Einträge.")
        while True:
            try:
                sleep(5)
                print("Menü")
                for i in menü:
                    print(i)
                sleep(5)
                auswahl = int(input("Was wollen Sie machen: "))
                sleep(3)
                if auswahl < 1 or auswahl > len(menü):
                    raise Exception
                match auswahl:
                    case 1:
                        tabelle_zeigen()
                        sleep(4.5)
                    case 2:
                        artikel_hinzufügen()
                        sleep(5)
                    case 3:
                        tabelle_aktualisieren()
                        sleep(5)
                    case 4:
                        artikel_löschen()
                        sleep(5)
                    case 5:
                        raise KeyboardInterrupt
            except KeyboardInterrupt:
                print("Programm wird beendet...")
                return programm_beenden()
            except Exception:
                print("Ungültige Eingabe!")
    except KeyboardInterrupt:
        print("Programm wird beendet...")
        return programm_beenden()
    except:
        sleep(1)
        print("Ein Fehler ist aufgetreten!")
        return exit(-1)
if __name__ == "__main__":
    main()