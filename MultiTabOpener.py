import webbrowser
from colorama import init, Fore

init(autoreset=True)

def print_ascii_art():
    print(Fore.RED + '________        ________                              .__        __ ')
    print(Fore.RED + '\\______ \\_______\\_____  \\__  _  __ ___________   ____ |__|____  |  | __ ')
    print(Fore.RED + "|    |  \\_  __ \\/  / \\  \\ \\/ \\/ // __ \\_  __ \\_/ ___\\|  \\__  \\ |  |/ / ")
    print(Fore.RED + "|    `   \\  | \\/   \\_/.  \\     /\\  ___/|  | \\/\\  \\___|  |/ __ \\|    <")
    print(Fore.RED + "/_______  /__|  \\_____\\ \\_/\\/\\_/  \\___  >__|    \\___  >__(____  /__|_ \\ ")
    print(Fore.RED + "        \\/             \\__>           \\/            \\/        \\/     \\/")

def open_multiple_tabs(url, tab_count):
    try:
        for _ in range(tab_count):
            webbrowser.open_new_tab(url)
    except webbrowser.Error:
        print("Nie udało się otworzyć przeglądarki lub karty na wskazany adres. Sprawdź, czy adres URL jest prawidłowy.")

def main():
    print_ascii_art()
    while True:
        url = input("Podaj adres strony: ")
        try:
            tab_count = int(input("Podaj liczbę Kart: "))
            open_multiple_tabs(url, tab_count)
            print("Ukończono ładowanie stron.")
        except ValueError:
            print("Podano nieprawidłową liczbę kart.")

        repeat = input("Czy chcesz powtórzyć działanie? (Y/N): ").upper()
        if repeat != "Y":
            break

if __name__ == "__main__":
    main()
