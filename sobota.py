print("piekny dzien - numer 1")

def wypisz_imie(my_name):
    if my_name == "Ania":
        return my_name
    else:
        return "Błąd"

imie = wypisz_imie(input("Wpisz imię: "))

print(imie)