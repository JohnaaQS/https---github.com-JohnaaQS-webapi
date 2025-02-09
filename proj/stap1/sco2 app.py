import functies as api
import re

while True :
    print("\n_______________________________________________________________")
    print("welkom bij het keuzemenu")
    print("____________________________________________________________")
    print("1. Bekijk alle wijken.")
    print("2. Zoek informatie over een specifieke wijk.")
    print("3. Geef alle forces.")
    print("4. Geef straatcriminaliteit op basis van locatie.")
    print("5. Bekijk alle politiediensten.")
    print("6. Stop en zoek incidenten.")
    print("7. Stop het programma.")
    keuze = input("\nMaak een keuze: ")
    print("_______________________________________________________________")
    
    wijken = api.forces()
        
    if keuze == "1":
        wijken = api.neighbourhoods()
        if "error" in wijken:
            print(wijken["error"])
        else:
            print("\nOverzicht van wijken in Leicestershire:")
            print("_______________________________________________________________")
            for wijk in wijken:
                print(f"Naam: {wijk['name']} | Code: {wijk['id']}")
            print("_______________________________________________________________")

    elif keuze == "2":
        code = input("geef een wijkcode in (bv.'NC04'): ")
        wijk_info = api.specificneighbourhood(code)
        if "name" in wijk_info and "description" in wijk_info:
            naam = wijk_info["name"]
            beschrijving = wijk_info["description"]
            beschrijving = re.sub(r"<.*?>", "", beschrijving)
            print(f"Informatie over wijk '{naam}':")
            print(beschrijving)
        else:
            print("Geen informatie beschikbaar voor deze wijk.")
        
    elif keuze == "3":
        forces = api.forces()
        if "error" in forces:
            print(forces["error"])
        else:
            print("\nOverzicht van forces in Leicestershire:")
            print("_______________________________________________________________")   
        for force in forces:
            print(f"politieteam: {force['name']} | wijk: {force['id']}")
        print("_______________________________________________________________")
        
    elif keuze == "4":
        break