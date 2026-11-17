import requests

headers = {
    "User-Agent": "ASTROLOGIK/0.1 (contact: https://github.com/Aliss-13)"
}

def search_cities(city):

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": city,
        "format": "json",
        "limit": 5
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if not data:
            print("Ville introuvable")
            return

        # print(response.status_code)
        # print(data)

        return data

    except requests.exceptions.Timeout:
        print("Corinne de la géolocalisation est en plein commérage avec Michelle de la compta. Réessayez plus tard ! 💅")
        return None

    except requests.exceptions.RequestException as error:
        print(f"Erreur de géolocalisation : {error}")
        return None