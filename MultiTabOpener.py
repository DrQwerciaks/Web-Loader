import webbrowser

def open_multiple_tabs(url, tab_count):
    try:
        for _ in range(tab_count):
            webbrowser.open_new_tab(url)
    except webbrowser.Error:
        print("Nie udało się otworzyć przeglądarki lub karty na wskazany adres. Sprawdź, czy adres URL jest prawidłowy.")

def main():
    url = input("Podaj adres strony: ")
    try:
        tab_count = int(input("Podaj liczbę Kart: "))
        open_multiple_tabs(url, tab_count)
    except ValueError:
        print("Podano nieprawidłową liczbę kart.")

if __name__ == "__main__":
    main()
