import random
litery = "abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ"
znaki = "£!@#$%^&*()_+"
cyfry = "0123456789"

password = ""

i = 1
while i < 6: #pętla wylosuje po 5 znaków z każdej grupy: litery, znaki, cyfry łącznie 15 znaków
    password += str(random.choice(znaki))
    password += str(random.choice((litery)))
    password += str(random.choice((cyfry)))
    i += 1

#Tasowanie znaków, wynik zwróci listę
password_lista = random.sample(password, 15)

#konwersja listy na string
password_end = ""
for x in password_lista:
    password_end += str(x)

#wyświetlenie ostatecznego hasła
print("Hasło : ",password_end)
