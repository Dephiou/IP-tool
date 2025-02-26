import os
import sys

def ping_ip(ip_address):
    response = os.system(f"ping {ip_address} -n 4")
    if response == 0:
        print(f"Ping réussi pour {ip_address}")
    else:
        print(f"Ping échoué pour {ip_address}")

def main():
    ip_address = input("Entrez l'adresse IP à tester avec le ping : ").strip()
    if not ip_address:
        print("Aucune adresse IP fournie.")
        return

    ping_ip(ip_address)

    input("\nAppuyez sur Entrée pour revenir au menu principal...")
    os.system('cls')
    os.system('python main.py')

if __name__ == "__main__":
    main()
