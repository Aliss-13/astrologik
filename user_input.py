from display import DIM, RESET, YELLOW


def get_date_and_time():

    while True:

        try:
            start_time = input("Entrez une date et une heure (AAAA-MM-JJ HH:MM) : ")
            return start_time

        except ValueError:
            print("Saisie invalide.")


def get_city_name():

    city = input(f"Ville à rechercher {DIM}(Entrée pour revenir){RESET} : ").strip()

    if not city:
        return
        
    return city
    

def get_city_data(available_cities):

    while True:

        choice = input(f"Ville choisie {DIM}(Entrée pour revenir){RESET} : ").strip()
        print()

        if not choice:
            return

        # récupération de l'equipment_id
        if choice.isdigit() and 1 <= int(choice) <= len(available_cities):
            city_data = available_cities[int(choice) - 1]
            break

        print("Choix invalide. Recommencer ou Entrée pour revenir.")

    return city_data



def ask_ambiguous_time():

    print()
    print(f"{YELLOW}⚠️  Jean-Michel Apeuprès a détecté une anomalie temporelle !{RESET}")
    print("Votre heure de naissance correspond à deux horaires possibles :")
    
    while True:
    
        print("[1] Première occurrence") 
        print("[2] Deuxième occurrence")
        print("[3] La réponse D : calculer les deux versions")
    
        choice = input("> ")
        print()
    
        if choice in ("1", "2", "3"):
            return choice