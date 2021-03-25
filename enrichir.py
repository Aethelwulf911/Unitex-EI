# BOUSSOURA              Mohamed Cherif             - 181832022492
# FAZEZ                  Said Massinissa            - 181831029050
# L3 ACAD A 
import re,sys
from string import ascii_uppercase #importer une set de l'alphabet en ascii

crps=open(sys.argv[1],"r",encoding="utf-8") # ouverture de fichier corpus-medical.txt
subst = open("subst.dic", "r", encoding="utf-16-le") # ouverture de fichier subst.dic
subst_en = open("subst_enri.dic", "w", encoding="utf-16-le") # ouverture de fichier subst.dic
subst_en.write('\ufeff') # BOM
inter = []
mtr = crps.read()
#trouver tous les médicaments qui commence avec lettre majuscule
#avec plus de 1 a 3 mots + noumbre real ou entire
#avec  la unité ou : plus nombre plus /j| le matin| matin| le soir| soir| sachets| sachet| amp| amps| goutte| le midi | UI| le matin | par jour| le soir| g| mg
#ou nombre de forme 1-1-1-1
medoc1 = re.findall('[A-Z][a-zA-Z]+ ?[a-zA-Z]* ?[a-zA-Z]*(?: | )[0-9]*(?:[0-9]+[,.]?[0-9]* (?:mg/mL|mg/ml|mg/m²|g/m²|µg|mg|g|ml|l|µ|cp|s |ui/l|ui|UI|MG)[^/l]|: [0-9]*(?:/j| le matin| matin| le soir| soir| sachets| sachet| amp| amps| goutte| le midi | UI| le matin | par jour| le soir| g| mg)|[0-9]+[.,-][0-9]+[.,-][0-9]+ |: [0-9]+[.,-][0-9]+[.,-][0-9]+ )',mtr)

#trouver les médicaments avec lettre minuscule 
medoc2=re.findall('[a-zA-Z]+ ?[a-zA-Z]* ?[a-zA-Z]*(?: | )[0-9]*(?: | )[0-9]*(?:/j| le matin| matin| le soir| soir| sachets| sachet| amp| amps| goutte| le midi | le matin | par jour| le soir| g| mg)',mtr)
medoc = []
print(medoc2)
#boucle pour ajouter les médicament à inter
for m in medoc1:
    #éviter les faux médicaments
    if (not (str(str(m).lower()).__contains__("eau") or str(str(m).lower()).__contains__("litres") or str(
            str(m).lower()).__contains__("voie") or str(str(m).lower()).__contains__(" le") or str(
            str(m).lower()).__contains__(" par") or str(str(m).lower()).__contains__(" et") or str(
            str(m).lower()).__contains__(" sous") or str(str(m).lower()).__contains__(" irm") or str(
            str(m).lower()).__contains__(" depuis") or str(str(m).lower()).__contains__(" lunettes") or str(
            str(m).lower()).__contains__(" novembre") or str(str(m).lower()).__contains__("vgm ") or str(
            str(m).lower()).__contains__("bilirubine") or str(str(m).lower()).__contains__("per ") or str(
            str(m).lower()).__contains__("avec ") or str(str(m).lower()).__contains__("hospital") or str(
            str(m).lower()).__contains__("iv") or str(str(m).lower()).__contains__(" de ") or str(
            str(m).lower()).__contains__("crp ") or str(str(m).lower()).__contains__("du "))):
        strr = str(re.sub("(?: | )[0-9]*(?:[0-9]+[,.]?[0-9]* (?:mg/mL|mg/ml|mg/m²|g/m²|µg|mg|g|ml|l|µ|cp|s |ui/l|ui|UI|MG)[^/l]|: [0-9]*(?:/j| le matin| matin| le soir| soir| sachets| sachet| amp| amps| goutte| le midi | UI|le matin | par jour| le soir| g| mg)|[0-9]+[.,-][0-9]+[.,-][0-9]+ |: [0-9]+[.,-][0-9]+[.,-][0-9]+)","", m, flags=re.I)).lower()
        subst_en.write(strr + "\n")
        inter.append(strr)#ajouter les médicament à inter
#boucle pour ajouter les médicament à inter
for m in medoc2:
    # éviter les faux médicaments
    if not (str(str(m).lower()).__contains__("mg ") or str(str(m).lower()).__contains__("j ") or str(str(m).lower()).__contains__("et ") or str(str(m).lower()).__contains__("mide ") or str(str(m).lower()).__contains__("dose ") or str(str(m).lower()).__contains__("ration ")):
        strr = str(re.sub("(?: | )[0-9]*(?: | )[0-9]*(?:/j| le matin| matin| le soir| soir| sachets| sachet| amp| amps| goutte| le midi | le matin | par jour| le soir| g| mg)","", m, flags=re.I)).lower()

        subst_en.write(strr + "\n")
        inter.append(strr) #ajouter les médicament à inter


inter2 = []
subst_en.close()
subst_en = open("subst_enri.dic", "r", encoding="utf-16-le") # ouverture de fichier subst.dic
nb=0
#affichage les medicament de subst_enri
for i in subst_en :
  nb+=1
  print(str(nb)+" "+i)
#ajouter les medicament de courps dans inter2

for i in inter:
    if i not in inter2:
        inter2.append(i)
infos3 = open('infos3.txt', 'w+', encoding='utf-8')
infos2 = open('infos2.txt', 'w+', encoding='utf-8')
ldd=0
inter2.sort()
#ecrire dans fichier file2
for letter in ascii_uppercase:       #compter le nombre de substances par lettre de l'alphabet
    a = 0
    nbLettre=0
    for el in inter2:
        if letter == el[0].upper() or (letter=="E" and el[0]=="é"):
            nbLettre+=1
            infos2 = open('infos2.txt', 'r+', encoding='utf-8').readlines()
            for i in infos2:
                if str(el).upper() == str(i).upper() :
                    a = 1
            infos2 = open('infos2.txt', 'a+', encoding='utf-8')
            if a == 0:
                infos2.write(str(el)+",.N+subst\n")
    infos2.write(' _____________________________________________________\n')
    infos2.write('|Nombre d\'entrées dans '+letter+': '+str(nbLettre)+'|\n')
    infos2.write(' _____________________________________________________\n')
infos2.write('Nombre d\'entrées total: '+str(len(inter2)))
inter.clear()

for i in subst:
    m = i.split(",")

    inter.append(m[0].replace("\ufeff",""))
inter3 = []
#ajouter les medicament de enrichissement  dans inter3
for i in inter2:
    if i not in inter:
        inter3.append(i)
inter2.sort()
print(inter2)


#ecrire dans fichier file3
for letter in ascii_uppercase:
    a = 0
    nbLettre = 0
    for el in inter3:
        if letter == el[0].upper() or (letter=="E" and el[0]=="é"):
            nbLettre+=1
            infos3 = open('infos3.txt', 'r+', encoding='utf-8').readlines()
            for i in infos3:
                if str(el).upper() == str(i).upper() :
                    a = 1
            infos3 = open('infos3.txt', 'a+', encoding='utf-8')
            if a == 0:
                infos3.write(str(el)+",.N+subst\n")
    infos3.write(' _____________________________________________________\n')
    infos3.write('|Nombre d\'entrées dans '+letter+': '+str(nbLettre)+'|\n')
    infos3.write(' _____________________________________________________\n')
infos3.write('Nombre d\'entrées total: '+str(inter2.__len__()))
subst.close()

subst = open("subst.dic", "w", encoding="utf-16-le") # ouverture de fichier subst.dic
subst.write('\ufeff') # BOM

for i in inter:
    inter2.append(i)
#ecrire dans fichier subst
for letter in ascii_uppercase:


    for el in inter2:
        if letter == el[0].upper() or (letter == "E" and el[0] == "é"):
          subst.write(el.replace("\n","")+ ",.N+subst\n")



#Traitement hospitalier
#TRAITEMENT À DOMICILE CYTARABINE 40 mg METHOTREXATE 3 g/m² DOXORUBICINE 50 mg/m² Inexium 40mg pipéracilline-tazobactam 4g
#TRAITEMENT DE SORTIE
#interne chirurgie
