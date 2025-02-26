import requests
import os

def get_ip_location(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"status": "fail", "message": str(e)}

def print_location_info(location_info):
    """Affiche les informations de localisation IP"""
    if location_info['status'] == 'success':
        print("\nInformations de localisation :")
        print(f"Adresse IP : {location_info.get('query', 'Non disponible')}")
        print(f"Pays : {location_info.get('country', 'Non disponible')}")
        print(f"Région : {location_info.get('regionName', 'Non disponible')}")
        print(f"Ville : {location_info.get('city', 'Non disponible')}")
        print(f"Latitude : {location_info.get('lat', 'Non disponible')}")
        print(f"Longitude : {location_info.get('lon', 'Non disponible')}")
    else:
        print(f"Erreur : {location_info.get('message', 'Non disponible')}")

def main():
    ip_address = input("Entrez l'adresse IP à localiser : ").strip()
    if not ip_address:
        print("Aucune adresse IP fournie.")
        return

    location_info = get_ip_location(ip_address)
    print_location_info(location_info)

    input("\nAppuyez sur Entrée pour revenir au menu principal...")
    os.system('cls')
    os.system('python main.py')

if __name__ == "__main__":
    main()
