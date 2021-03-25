# BOUSSOURA              Mohamed Cherif             - 181832022492
# FAZEZ                  Said Massinissa            - 181831029050
# L3 ACAD A 
import re, sys
from bs4 import BeautifulSoup
# urllib est un paquet qui collecte plusieurs modules travaillant avec les URLs
from urllib.request import urlopen  # pour ouvrir et lire des URLs

# Le cas ou utilisateur donne rien dans les arguments d'entrer
if len(sys.argv) == 1:
    print("Erreur vous avez oublie les arguments d'entrer !")
    sys.exit()
# Le cas ou utilisateur donne intervalle et le port dans les arguments
if len(sys.argv) == 3:
    # Tester intervalle s'il correcte (dans la forme ou le premier caractere est sup que le deuxieme)
    if re.match("[A-Z]-[A-Z]", sys.argv[1]) and sys.argv[1][0] <= sys.argv[1][2]:
        Borne_inf = ord(sys.argv[1][0])
        Borne_sup = ord(sys.argv[1][2])
        port = sys.argv[2]
    # Affichage le message d'erreur dans le cas ou erreur dans l'intervalle (mal choisi l'intervalle)
    else:
        print("Erreur dans les arguments d'entrer !")
# Le cas ou utilisateur donne qu'un seule argument le port
else:
    port = sys.argv[1]
    Borne_inf = ord("A")
    Borne_sup = ord("Z")
cpt = 0  # cette varibale pour calculer la totalite des midoc dans le fichier infos.txt
info = open("infos.txt", "w")  # ouverture de fichier infos.txt
subst = open("subst.dic", "w", encoding="utf-16-le")  # ouverture de fichier subst.dic
subst.write('\ufeff')  # BOM
# Remplissage les deux fichier
for z in range(Borne_inf, Borne_sup + 1):
    # Ouverture le
    f = urlopen("http://127.0.0.1:" + port + "/vidal/vidal-Sommaires-Substances-" + chr(z) + ".htm")
    print("\n"+"URL ==>http://127.0.0.1:" + port + "/vidal/vidal-Sommaires-Substances-" + chr(z) + ".htm \n")
    x = f.read()
    print(str(x))

    # on met le decode pour ne changer pas le type de fichier (UTF-8 SANS BOM)
    medoc = re.findall("[0-9]+\.htm\">.+<", x.decode("utf-8"))  # rechercher tout les mots avec cette regex
    f.close()  # fermeture
    # Remplissage le fichier subts.dic
    for i in medoc:
        y = re.sub("<", "", re.sub("[0-9]+\.htm\">", "", i, flags=re.I), flags=re.I)
        subst.write(y + ",.N+subst\n")

    # Remplissage le fichier infos.txt
    info.write("Total de " + chr(z) + " : " + str(len(medoc)) + "\n")
    cpt = cpt + len(medoc)
subst.close()
info.write("Le nombre total des subtances actives est : " + str(cpt))
info.close()
