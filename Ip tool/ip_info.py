import requests
import os

def get_location_info(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        response.raise_for_status()
        location_info = response.json()

        results = []
        if location_info.get('status') == 'success':

            results.append("\nInformations de localisation pour l'adresse IP :")
            results.append(f"  Adresse IP : {location_info.get('query', 'Non disponible')}")
            results.append(f"  Pays : {location_info.get('country', 'Non disponible')} ({location_info.get('countryCode', 'Non disponible')})")
            results.append(f"  Continent : {location_info.get('continent', 'Non disponible')} ({location_info.get('continentCode', 'Non disponible')})")
            results.append(f"  Région : {location_info.get('regionName', 'Non disponible')} ({location_info.get('region', 'Non disponible')})")
            results.append(f"  Ville : {location_info.get('city', 'Non disponible')}")
            results.append(f"  Code postal : {location_info.get('zip', 'Non disponible')}")
            results.append(f"  Latitude : {location_info.get('lat', 'Non disponible')}")
            results.append(f"  Longitude : {location_info.get('lon', 'Non disponible')}")
            results.append(f"  Fuseau horaire : {location_info.get('timezone', 'Non disponible')}")
            results.append(f"  Devise : {location_info.get('currency', 'Non disponible')}")
            results.append(f"  FAI : {location_info.get('isp', 'Non disponible')}")
            results.append(f"  Organisation : {location_info.get('org', 'Non disponible')}")
            results.append(f"  AS : {location_info.get('as', 'Non disponible')}")
            results.append(f"  Mobile : {location_info.get('mobile', 'Non disponible')}")
            results.append(f"  Proxy : {location_info.get('proxy', 'Non disponible')}")
            results.append(f"  Hébergement : {location_info.get('hosting', 'Non disponible')}")
        else:
            results.append(f"Erreur : {location_info.get('message', 'Message d’erreur non disponible')}")
    except requests.exceptions.RequestException as e:
        results.append(f"Erreur lors de la requête à l'API : {e}")


    print("\n".join(results))

def main():
    ip_address = input("Entrez l'adresse IP à localiser : ").strip()
    if not ip_address:
        print("Aucune adresse IP fournie.")
        return

    get_location_info(ip_address)

    input("\nAppuyez sur Entrée pour revenir au menu principal...")
    os.system('cls')
    os.system('python main.py')

if __name__ == "__main__":
    main()
