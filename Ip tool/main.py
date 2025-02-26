import subprocess

def run_script(script_name):
    """Exécute un script Python externe."""
    try:
        subprocess.run(['python', script_name], check=True)
        print(f"{script_name} exécuté avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de {script_name}: {e}")
    except Exception as e:
        print(f"Erreur inconnue: {e}")

def main():
    # Menu d'options
    print("Choisissez un script à exécuter :")
    print("1. Localiser IP")
    print("2. Informations sur IP")
    print("3. Ping IP")
    
    choice = input("Entrez le numéro du script que vous voulez exécuter (1, 2, ou 3) : ").strip()

    if choice == '1':
        run_script("ip_location.py")
    elif choice == '2':
        run_script("ip_info.py")
    elif choice == '3':
        run_script("ping_ip.py")
    else:
        print("Choix invalide, veuillez entrer 1, 2, ou 3.")

if __name__ == "__main__":
    main()
