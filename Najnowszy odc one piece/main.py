import requests
from bs4 import BeautifulSoup

#Otwieranie strony
url = requests.get("https://shinden.pl/titles/12-one-piece/episodes")
doc = BeautifulSoup(url.text, "html.parser")

#Znalezienie id danych
find = doc.find_all(class_="ep-title")
odcinki = find[1].parent
id_poprzedniego_odc = find[2].parent
odcinki1 = odcinki.find(class_="ep-title")
poprzedniodc = id_poprzedniego_odc.find(class_="ep-title")
nrpoprzedniegoodcinka = id_poprzedniego_odc.find("td").string
nrodcinka = odcinki.find("td").string

#Pobranie danych z pliku
file = open('Dane.TXT', 'r')
odczyt = file.readline()
file.close()

#Wyswietlanie czy jest odcinek czy jeszcze nie
print("")
if nrodcinka != odczyt:
    print("JEST!!!!")
elif nrodcinka == odczyt:
    print("Niestety jeszcze nie ma :c")

#Zapisanie danych do pliku
nrodcinka_dopliku = nrodcinka
file = open('Dane.TXT', 'w')
file.write(nrodcinka_dopliku)
file.close()

#Wyswietlanie wynikow
print("")
print("Najnowszy odcinek to: ", odcinki1.string)
print("Numer odcinka : ", nrodcinka)
print("")
print("Jak coś to poprzedni odcinek to: ", poprzedniodc.string)
print("Numer odcinka: ", nrpoprzedniegoodcinka)
print("")
input("Naciśnij ENTER aby wyjść")