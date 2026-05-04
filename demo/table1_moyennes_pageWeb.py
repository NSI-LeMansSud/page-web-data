# table1.csv, fichier de notes d'élèves (fictifs) en anglais, info et maths.
# en sortie un fichier moyenne.html que l'on peut ouvrir dans un navigateur
# moyenne.html affiche un tableau (très moche pour la démo) comportant la
# moyenne des 3 notes pour chaque élève.

import csv # CSV : Comma Separated Values

table1 = []
with open('table1.csv', encoding='utf8', newline='') as fnotes :
    lecteur = csv.DictReader(fnotes, delimiter=',', quotechar="'")
    compteur = 0
    for ligne in lecteur :
        table1.append(dict(ligne))
        if compteur < 10:
            print(ligne)
            compteur = compteur + 1

#print(table1) # table1 = liste de dictionnaires



with open('moyenne.html', 'w') as html: # 'w' pour write, fichier en écriture
    html.write ("""
                <!DOCTYPE html>
                <html lang='fr'>
                  <head>
                    <title>Titre affiché dans la barre de titre du navigateur</title>
                  </head>
                  <body>
                    <p> C'est ici que vous mettrez votre contenu  </p>
                """)
    html.write("""<table>
                        <tr>
                            <th>Nom</th>
                            <th>Moyenne</th>
                        </tr>
                """)
    for eleve in table1: #lignes du tableau
        html.write("<tr> \n") # \n = saut de ligne
        html.write("<td>" + eleve['Nom'] + "</td> \n")
        anglais, maths, info = int(eleve['Anglais']), int(eleve['Maths']), int(eleve['Info'])
        moyenne = (anglais + maths + info) / 3
        html.write("<td>" + str(moyenne) + "</td> \n")
        html.write("</tr> \n")

    html.write("""</table>
                    </body>
                  </html>
                """)


