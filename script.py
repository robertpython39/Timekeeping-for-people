#-------------------------------------------------------------------------------
# Name:        Timekeeping for People
# Purpose:    
#
# Author:      nicolescu
#
# Created:     05/02/2022
# Copyright:   (c) nicol 2022
# Licence:     
#-------------------------------------------------------------------------------


from datetime import *
import os
import sys
import getpass


# TODO Calea unde se va salva fisierul text (Desktop)
username = getpass.getuser()
folder_gol = os.path.expanduser("~") + r"\Desktop\Pontaj " + str(username)
path = folder_gol
if not os.path.exists(path):
    os.makedirs(path)

# # TODO Colectare date despre angajat (nume, user, ora intrare/iesire, numar total de ore lucrate) + verificare daca exista deja fisierl text creat
# TODO daca exista fisierul text creat, informatia se va adauga in el, in continuare (append)

if not os.path.isfile(path+r"\Pontaj_" + str(username) + ".txt"):
    with open((path+r"\Pontaj_" + str(username) + ".txt"), "w") as f:
        nume_complet = input("Introduceti numele d-voastra: ").title()
        f.write("Nume:" + nume_complet)
        f.write("\n")
        user = input("Introduceti userul: ").lower()
        f.write("User:<<" + user + ">>")
        f.write("\n")
        ora_intrare = input("Introduceti ora intrare(in format HH:MM): ") + ":00"
        f.write("Ora intrare:" + ora_intrare)
        f.write("\n")
        ora_iesire = input("Introduceti ora iesire/terminare program de lucru(in format HH:MM): ") + ":00"
        f.write("Ora iesire:" + ora_iesire)
        f.write("\n")
        start_dt = datetime.strptime(ora_intrare, '%H:%M:%S')
        end_dt = datetime.strptime(ora_iesire, '%H:%M:%S')
        diff = (end_dt - start_dt)
        total_ore = round(diff.seconds / 60 / 60, 2)
        today = date.today()
        f.write("Ore lucrate in data de " + str(today) + ": " + str(total_ore) + " ore")
        f.write("\n")
        f.write("_____________________________________________________________________________________")
        f.write("\n")
        f.close()
else:
    with open((path+r"\Pontaj_" + str(username) + ".txt"), "a") as f:
        nume_complet = input("Introduceti numele d-voastra: ").title()
        f.write("Nume:" + nume_complet)
        f.write("\n")
        user = input("Introduceti userul: ").lower()
        f.write("User:<<" + user + ">>")
        f.write("\n")
        ora_intrare = input("Introduceti ora intrare(in format HH:MM): ")+":00"
        f.write("Ora intrare:" + ora_intrare)
        f.write("\n")
        ora_iesire = input("Introduceti ora iesire/terminare program de lucru(in format HH:MM): ")+":00"
        f.write("Ora iesire:" + ora_iesire)
        f.write("\n")
        start_dt = datetime.strptime(ora_intrare, '%H:%M:%S')
        end_dt = datetime.strptime(ora_iesire, '%H:%M:%S')
        diff = (end_dt - start_dt)
        total_ore = round(diff.seconds / 60 / 60,2)
        today = date.today()
        f.write("Ore lucrate in data de " + str(today) + ": " + str(total_ore) +  " ore")
        f.write("\n")
        f.write("_____________________________________________________________________________________")
        f.write("\n")
        f.close()


print("O zi buna!")
exit = input("Apasa orice tasta pentru iesire.....")


