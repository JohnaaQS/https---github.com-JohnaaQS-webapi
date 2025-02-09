import functies as api
import re, random


#Toon gebruiker alle forces
forces = api.forces()
forces_names = []
print("\nOverzicht van steden:")
print("_______________________________________________________________")   
for force in forces:
    print(f"wijk: {force['id']}")
    forces_names.append(force['id'])
print("_______________________________________________________________")
        
             
while True:   
    #wijk controlle  
    hood = input("kies 1 optie uit de lijst? ")
    if hood in forces_names:
        print(f"top, je hebt de wijk {hood} gekozen, laten we van start gaan!")
        break
    elif hood not in forces_names:
        print("onbetsaande force")


while True :
    #keuze menu
    print("\n_______________________________________________________________")
    print("welkom bij het keuzemenu")
    print("____________________________________________________________")
    print("1. Wijzig wijk.")
    print("2. zoek een wijkcode.")
    print("3. Zoek informatie over een specifieke wijk")
    print("4. Geef straatcriminaliteit op basis van locatie.")
    print("5. Stop het programma.")
    keuze = input("\nMaak een keuze: ")
    print("_______________________________________________________________")
    
    if keuze == "1":
        forces = api.forces()
        if "error" in forces:
            #checken of er error is
            print(forces["error"])
        else:
            #overzicht van alle wijken 
            print("\nOverzicht van steden:")
            print("_______________________________________________________________")   
        for force in forces:
            print(f"wijk: {force['id']}")
        print("_______________________________________________________________")
        hood = input("kies 1 optie uit de lijst ")
  
    if keuze == "2":
        wijken = api.neighbourhoods(hood)
        if "error" in wijken:
            #checken of er error is
            print(wijken["error"])
        else:
            #de wijken en wijkcodes 
            print(f"\nOverzicht van wijken in de steden {hood}:")
            print("_______________________________________________________________")
            for wijk in wijken:
                #codes van alle wijken geven 
                print(f"Naam: {wijk['name']} | Code: {wijk['id']}")
            print("_______________________________________________________________")

    elif keuze == "3":
        code = input("geef een wijkcode in (bv.'NC04'): ")
        wijk_info = api.specificneighbourhood(hood,code)
        if "name" in wijk_info and "description" in wijk_info:
            naam = wijk_info["name"] #naam van de wijk wegschrijven
            beschrijving = wijk_info["description"] # beschrijvinf van de wijk wegschrijven
            # de rare tekens uit de tekst halen 
            beschrijving = re.sub(r"<.*?>", "", beschrijving)
            print(f"Informatie over wijk '{naam}':")
            print(beschrijving)
        else:
            #geen info gevonden
            print("Geen informatie beschikbaar voor deze wijk.")
        
    elif keuze == "4":
        crimes = api.crimes_no_loc(hood)
        #aantal crimes opslaan
        aantalcrimes = len(crimes)
        if "error" in crimes:
            print(crimes["error"])
        #kleiner dan of gelijk aan 5 crimesd worden ze allemaal gegeven
        elif len(crimes) <= 5:
            crimes = random.sample(crimes, aantalcrimes)
            print("crimes gebasseerd op de wijk.")
            for crime in crimes:
                print(f"catogorie: {crime['category']} | outcome: {crime['outcome_status']['category']}")
            print("_______________________________________________________________")
        #5 en meer crimes worden er random een 5 tal gepakt ui de lijst.
        else: 
            crimes = random.sample(crimes, 5)
            print("crimes gebasseerd op de wijk.")
            print("_______________________________________________________________")
            print("teveel crimes, ik geef er 5 mee:")
            for crime in crimes:
                print(f"catogorie: {crime['category']} | outcome: {crime['outcome_status']['category']}")
            print("_______________________________________________________________") 
            
    elif keuze == "5":
        print("bedankt voor het gebruiken van de app, tot ziens!")
        break
    
    else:
        print("geef een optie uit de lijst, als je wilt afsluiten geef 5.")