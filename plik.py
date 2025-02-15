# Zmienne
liczba = 6
zmiennoprzecinkowa = 8.5
napis = "Tekst"
logiczna = True

print(f"Liczba: {liczba}, liczba z przecinkiem: {zmiennoprzecinkowa}, napis: {napis}, logiczna: {logiczna}")

liczba = "sześć"
print(f"Zmienna liczba jest typu {type(liczba)}")

# Listy
gry = ["minecraft", "roblox"]
lista_mieszana = [1, "minecraft", True]
lista_w_liscie = [1, ["element_listy", 3, True]]

print(gry)
print(lista_mieszana)

gry.append("Mario")

print(gry)

# Pętle
licznik = 0
print("Pętla while licząca do 5")

while licznik <=5:
  print(licznik)
  licznik = licznik + 1

print("Pętla for licząca do 7")
for liczba in range(8):
  print(liczba)

# Instrukcje warunkowe
temperatura = 20

if temperatura < 20:
  print("Jest zbyt zimno")
else:
  print("Jest okej")