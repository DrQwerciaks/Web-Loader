import webbrowser
from colorama import init, Fore

init(autoreset=True)

def print_ascii_art():
    gray = Fore.LIGHTBLACK_EX  # Jasnoszary kolor

    print(gray + "________        ________                              .__        __ ")
    print(gray + "\\______ \\_______\\_____  \\__  _  __ ___________   ____ |__|____  |  | __ ")
    print(gray + " |    |  \\_  __ \\/  / \\  \\ \\/ \\/ // __ \\_  __ \\_/ ___\\|  \\__  \\ |  |/ / ")
    print(gray + " |    `   \\  | \\/   \\_/.  \\     /\\  ___/|  | \\/\\  \\___|  |/ __ \\|    <")
    print(gray + "/_______  /__|  \\_____/\\ \\_/\\/\\_/  \\___  >__|    \\___  >__(____  /__|_ \\ ")
    print(gray + "        \\/             \\__>           \\/            \\/        \\/     \\/")
    print(gray + "   _____        .__   __  ._____________     ___.    ________ ")
    print(gray + "  /     \\  __ __|  |_/  |_|__\\__    ___/____ \\_ |__  \\_____  \\ ______   ____   ____   ___________ ")
    print(gray + " /  \\ /  \\|  |  \\  |\\   __\\  | |    |  \\__  \\ | __ \\ /   |   \\\\____ \\_/ __ \\ /    \\_/ __ \\_  __ \\")
    print(gray + "/    Y    \\  |  /  |_|  | |  | |    |   / __ \\| \\_\\ \\/    |    \\  |_> >  ___/|   |  \\  ___/|  | \\/")
    print(gray + "\\____|__  /____/|____/__| |__| |____|  (____  /___  /\\_______  /   __/ \\___  >___|  /\\___  >__|")
    print(gray + "        \\/                                  \\/    \\/         \\/|__|        \\/     \\/     \\/")

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

