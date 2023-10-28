import tkinter as tk
from tkinter import messagebox
import webbrowser
import time
import requests

def open_url():
    url = url_entry.get()
    try:
        tab_count = int(tab_count_entry.get())
        delay = float(delay_entry.get())
        for _ in range(tab_count):
            webbrowser.open_new_tab(url)
            time.sleep(delay)
        messagebox.showinfo("Sukces", "Zakończono otwieranie kart.")
    except ValueError:
        messagebox.showwarning("Błąd", "Nieprawidłowa liczba kart lub opóźnienie.")

# Ustawienie głównego okna
root = tk.Tk()
root.title("Otwieracz Kart")

# Etykiety i pola tekstowe
tk.Label(root, text="Adres URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Label(root, text="Liczba kart:").pack()
tab_count_entry = tk.Entry(root, width=5)
tab_count_entry.pack()

tk.Label(root, text="Opóźnienie (sekundy):").pack()
delay_entry = tk.Entry(root, width=5)
delay_entry.pack()

# Przycisk
open_button = tk.Button(root, text="Otwórz karty", command=open_url)
open_button.pack()

# Uruchomienie pętli zdarzeń
root.mainloop()
