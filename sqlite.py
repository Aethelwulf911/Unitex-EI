# BOUSSOURA              Mohamed Cherif             - 181832022492
# FAZEZ                  Said Massinissa            - 181831029050
# L3 ACAD A 
import sqlite3,re                       # Importer des bibliotheques
from urllib.request import  urlopen     # On utilise url pour extraire les information d'apres le fichier generer concord.html
con = sqlite3.connect('extraction.db')  # Base de donnee dans le fichier "extraction.db"
cur = con.cursor()                      # Activer le curseur pour acceder au DB
idd = 1                                 # Initialiser le premier ID
# Executer Instruction CREATE pour créer la table EXTRACTION a des elements : entier ID non null et String POSOLOGIE aussi non null
cur.execute(""" CREATE TABLE EXTRACTION(
            ID INTEGER NOT NULL PRIMARY KEY,
            POSOLOGIE TEXT NOT NULL
            )""")
# Ouvrir le fichier concord.html
f = urlopen("file:///C:/Users/Aethelwulf/AppData/Local/Unitex-GramLab/App/corpus-medical_snt/concord.html")
medoc = re.findall("<a .*",f.read().decode("utf-8"))    # Extraire les informations qui ce trouve dans le fichier concord
for i in range(len(medoc)):                             # Boucler les information
	a = medoc[i].split(">")                             # Separer le balise fermant pour prendre le resultat
	print(str(idd)+"\t|\t"+a[1][0:len(a[1])-3])         # Afficher information
	cur.execute("INSERT INTO EXTRACTION VALUES("+str(idd)+",'"+a[1][0:len(a[1])-3]+"')") # Inserer information dans la table avec instruction INSERT
	idd+=1                                              # Incremanter le ID
f.close()                                               # Fermeture de urlopen
con.commit()                                            # Validation des modifications
con.close()                                             # Déconnexion