from tkinter import*
from random import*

fen=Tk()
fen.title("Mastermind")
fen.geometry("1020x900")
fen["bg"]="light blue"

L1=[]           # initialisation des listes
L2=[]
k=69            # initialisation d'un tableau de 70 cases allant de 0 à 69 
z=27            # initialisation d'un tableau de 28 cases allant de 0 à 27
coup = 0
verif=True
perdu=False


for i in range (0,5):       # création de la liste de couleurs choisies au hasard
    u=randint(0,6)
    L1=L1+[u]
print(L1)

# (Nouveau)
f0 = Frame(fen, bd=4, bg="light grey", height=250, width=500, relief="solid")   #création de la fenêtre frame f0 pour le titre
f0.place(x=500, y=20)

f1 = Frame(fen, bd=5, bg = '#80c0c0', relief="ridge")                           #création de la fenêtre frame f1 pour la grille de labels
f1.pack(side=LEFT, padx=10)                              

f2 = Frame(fen, bg="light blue")                                                #création de la fenêtre frame f2 pour les boutons de couleurs
f2.place(x=500, y=300)

f3 = Frame(fen, bd=5, bg= "light grey", relief="ridge")                         #création de la fenêtre frame f3 pour la grille de labels de validation
f3.pack(side=LEFT, pady=5,padx=5)

# (Nouveau)
f4 = Frame(fen,bd=3, height= 50, width=290, bg="light grey", relief="ridge")    #création de la fenêtre frame f4 pour les labels de solution
f4.place(x=12,y=60)

f5 = Frame(fen,bd=3, height= 50, width=290, bg="light blue")    #création de la fenêtre frame f5 pour les boutons d'actions
f5.place(x=700, y=375)

# (Nouveau)
Lab_score = Label(f0,width=30, height=3, bg="light grey")
Lab_score.place(x=110, y=180)

Lab_Titre=Label(f0, bd=3, text="MASTERMIND\n version 1.0",fg= "black", font="arial 20 italic",bg="grey", height=4, width=20, relief="groove")          #création du Titre
Lab_Titre.place(x=90, y=50)

#création de la grille de label pour les couleurs
Lab = [0]*70                                                                # création d'une liste Lab composéé de 70 zéros
for n in range (0,70):                                                      # boucle for remplaçant les 0 par des labels initialises à la couleur "blanc"
    Lab[n] = Label(f1, relief="sunken", width=5, height=2, bg = "white")
    i=n//5
    j=n%5
    Lab[n].grid(row=i, column=j, pady=5, padx=10)                           # définition de la position pour obtenir un tableau de 5 colonnes par 14 lignes

#création de la grille de label pour l'affichage de la vérification ( 1 label sur deux est blanc l'autre noir)    
Lab_valid = [0]*28                                                          # création d'une liste Lab_valid composéé de 28 zéros  
for n in range (0,28):
    if n%2 == 0:                                                                    # couleur du label (blanc ou noir) en fonction de la parité de n (pair ou impair) 
        Lab_valid[n] = Label(f3, relief="sunken", width=5, height=2, bg="white")    # label blanc pour le nombre de couleurs présentes bien placées 
    else :
        Lab_valid[n] = Label(f3, relief="sunken", width=5, height=2, bg="black")    # label noir pour le nombre de couleurs présentes mal placées
    i=n//2
    j=n%2
    Lab_valid[n].grid(row=i, column=j, pady=5, padx=10)                             # définition de la position pour obtenir un tableau de 2 colonnes par 7 lignes

# enregistrement des couleurs dans une liste    
col = [0]*7                                         # création d'une liste img composéé de 7 zéros
for (n, couleur) in [(0, 'yellow'),                  (1,'#5A5A5A'), 
                 (2, 'blue'), 
                 (3, 'orange'), 
                 (4, 'red'), 
                 (5, 'green'),
                 (6, '#7030A0')]:            # boucle for remplaçant les 0 par des images représentant les couleurs, formant un tableau d'items couleurs
    col[n] = couleur

# definition de la fonction affichant les couleurs
def couleur(n):                                         
    global k,verif, L2,perdu
    if (k+1)%5 != 0 or verif == True:                       # conditions d'entrée dans la boucle: il reste au moins une case non-colorée dans la ligne et ligne pas encore validée
        Lab[k].config(height=2,width=5 ,bg=col[n])     # modification du label Lab[k] avec l'image correspondant à la couleur choisie et redimensionnement par rapport à l'écran
        k=k-1                                               # k est le compteur de labels
        L2=[n]+L2                                           # L2 est la liste de nombres correspondant aux couleurs choisies par le joueur
        verif = False                                       
        if k==0:                                            # si le dernier label du tableau est rempli
            perdu = True                                    # variable "perdu" utilisée dans la procedure Valider()

#  (Nouveau): définition de la procédure permettant le redémarrage du jeu
def Redemarrer():
    global z,k,coup,verif,L1,L2,perdu
    # initialisation des variables
    L2=[]
    l=[]
    L1=[]
    coup=0
    verif = True
    perdu = False
    # re-création de la liste de couleurs choisies au hasard
    for i in range (0,5):   
        u=randint(0,6)
        L1=L1+[u]
    print(L1)
    # boucle for permettant de d'enlever les indcations des labels de vérification
    for i in range(z+1,28):
        Lab_valid[i].config(text="")
    # boucle for permettant de remplacer les images des labels contenant une image couleur par l'image blanche de suppression
    for i in range(k+1,70):
        Lab[i].config(bg="white")
    # initialisation des compteurs 
    k=69
    z=27

# (Nouveau): definition de la procédure de fin du programme 
def fin(x):
    global verif,coup
    # création de la liste solution de couleurs (même principe que les tableaux de labels) 
    Lab = [0]*5
    for n in range (0,5):
        a=L1[n]
        Lab[n] = Label(f4, relief="sunken", height=2,width=5, bg=col[a])                    # les labels comportant les couleurs qui correspondent à la liste choisie par l'ordinateur 
        Lab[n].grid(row=1,column=n,pady=5, padx=10)
    # création de la fenêtre de message de fin et du bouton pour "Rejouer"
    fen2 = Tk()
    fen2.geometry("190x70")
    if x==1:
        Lab_fin=Label(fen2, text="BRAVO \n vous avez réussi en {} coups".format(coup))
    else:
        Lab_fin=Label(fen2, text="PERDU \n vous avez epuisé tous vos essais")
    Lab_fin.grid(row=0, pady=5)
    # définition de la procédure "Rejouer"
    def Rejouer():
        fen2.destroy()
        for i in range(0,5):
            Lab[i].destroy()                    # supression de Labels solutions
        Redemarrer()                            # execution de la procédure "Redémarrer"
    But_Rejouer = Button(fen2, text="Rejouer", command = Rejouer).grid(row=1) 
    verif = False

def Valider():                                  #création de la procédure "valider"
    global coup,verif,z,L1,L2,perdu             #récupération des variables nécessaires à la procédure
    if (k+1)%5 == 0 and verif == False:                            #condition pour exécuter la procédure : toute la ligne doit être remplie
        verif = True                            #changement de la variable booléenne "verif"
        l=[]                                    #création de la liste temporaire "l"                
        blanc = 0                               #création des variables locales corespondant aux compteurs (type entier):
        noir = 0                                # blanc (nombre de couleurs présentes mais mal placées)
                                                # noir (nombre de couleurs présentes et bien placées)
        # boucle de réécriture de la liste L1 choisie par l'ordinateur dans une liste temporaire l
        for i in range (0,5):       
            l=l+[L1[i]]
        # Première boucle de vérification : compte le nombre de couleurs bien placées de la liste L2 en comparant les nombres associés aux couleurs
        for i in range(0,5):
            if L2[i] == l[i]:       # si à l'indice i les éléments des listes sont égaux
                l[i]=10             #   l'élément de l est remplacé par 10
                L2[i]=9             #   l'élément de L2 est remplacé par 9
                noir = noir + 1     # le compteur noir (nombre de couleurs bien placées) augmente de 1
        # Deuxième boucle de vérification : compte le nombre de couleurs présentes mais mal placées de la liste L2
        for i in range (0,5):
            if L2[i] in l:          # si à l'indice i l'élément de la liste L2 se trouve dans la liste l
                n=l.index(L2[i])    #   la premiere occurence ,de l'élément de L2 à l'indice i, présent dans la liste l est remplacé par 8 pour éviter  
                l[n]=8              #   de le recompter au prochain passage
                blanc = blanc + 1   # le compteur blanc (nombre de couleurs mal placées) augmente de 1
        coup = coup + 1             # le compteur de coups augmente de 1
        Lab_score.config(text="nombre de coups : " +str(coup))      # modification du label de score (affiche le nombre de coups joués)
        Lab_valid[z].config(text=blanc, fg="white")                 # modification des labels de vérfication, blancs et noirs avec les compteurs "noir" et "blanc"
        z=z-1                                                       #   (les noms des compteurs coresspondent à la couleur de la fonte d'écriture pas à la couleur de fond du label) 
        Lab_valid[z].config(text=noir, fg="black")
        z=z-1
        L2=[]                                                       # initialisation de la liste L2 pour le choix du joueur
        if noir == 5:                                               # si toutes les couleurs sont bien placées
            fin(1)                                                  #   exécution de la procédure fin(1) (cas de réussite)
        elif perdu == True and noir != 5  :                         # si toute les couleurs ne sont pas bien placées et que la dernière case du tableau est remplie
            fin(2)                                                  #   exécution de la procédure fin(2) (cas d'échec)

# définition de la procédure "supprimer" pour supprimer la dernière couleur du tableau
def supprimer():
    global k, verif
    if verif == False or (k+1)%5 != 0:                          # conditions pour exécuter la procédure: la variable booléenne de vérifiction doit être égale à faux
        k=k+1                                                   # ou le label ne doit pas appartenir à une nouvelle ligne
        Lab[k].config(bg="white")                         # le dernier label contenant une couleur est modifé pour afficher l'image blanche de supression
        del(L2[0])                                              # supression de la dernière valeur ajoutée à la liste L2
        verif = True

# (Nouveau) : définition de la procédure permettant d'afficher les règles du jeu
def Règles():
    fen1=Tk()                                       # création de la fenêtre
    fen1.title("Les Règles du jeu")
    fichier_règle = open("règles.txt")              # ouverture du fichier contenant les règles
    règle = fichier_règle.read()                    # enregistrement des règles
    Lab_regle = Label(fen1, text=règle).pack()      # affichage des règles dans un Label

# création d'une ligne de boutons (même principe que pour les tablaux de Labels)
But = [0]*7
for n in range (0,7):
    But[n] = Button(f2, bd=5, width=5, height=2, bg=col[n], command = lambda a=n: couleur(a))  # définitions des Boutons avec leur image et leur commande respectives par rapport à n
    But[n].grid(row=1, column=n, pady=5, padx=10)

# Création des boutons de menu avec leur commande respective
# (Nouveau)
Bout_Règle = Button(f5, bd=3, width=8, height=2, text="Les règles", command = Règles)
Bout_Règle.grid(row=2, column=3, pady=5, padx=10)

Bout_Valider = Button(f5, bd=3, width=7, height=2, text="Valider", command = Valider)
Bout_Valider.grid(row=3, column=3, pady=5, padx=10)

Bout_Supr = Button(f5, bd=3, width=9, height=2, text="Supprimer", command = supprimer)
Bout_Supr.grid(row=4, column=3, pady=5, padx=10)

# (Nouveau)
Bout_Redem = Button(f5, bd=3, width=9, height=2, text="Redémarrer", command = Redemarrer)
Bout_Redem.grid(row=5, column=3, pady=5, padx=10)

# (Nouveau)
Bout_Quitter = Button(f5, bd=3, width=7, height=2, text="Quitter", command = fen.destroy)
Bout_Quitter.grid(row=6, column=3, pady=5, padx=10)


fen.mainloop()               # lance le gestionnaire d'évènements
