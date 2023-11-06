import tkinter as tk
from tkinter import ttk
from regles import *
base_de_regles = {
    'regle1': {'antecedents': ['Une matrice carrée A a un déterminant non nul'], 'conclusion': 'A est inversible'},
    'regle2': {'antecedents': ['Une matrice A est inversible'], 'conclusion': 'L\'inverse de A est unique'},
    'regle3': {'antecedents': ['Une matrice A est symétrique', 'A est inversible'], 'conclusion': 'L\'inverse de A est également symétrique'},
    'regle4': {'antecedents': ['Une matrice A est diagonale'], 'conclusion': 'La matrice A est inversible si et seulement si tous les éléments diagonaux sont non nuls'},
    'regle5': {'antecedents': ['Une matrice A est échelonnée'], 'conclusion': 'A est inversible si tous les pivots sont non nuls'},
    'regle6': {'antecedents': ['Une matrice A est inversible'], 'conclusion': 'Le transposé de A est inversible'},
    'regle7': {'antecedents': ['Une matrice A est triangulaire supérieure', 'A est inversible'], 'conclusion': 'A est diagonale'},
}

########################################################################

def extraire_valeurs(base_de_regles):
    valeurs_regles = []

    for regle, details in base_de_regles.items():
        antecedents = details['antecedents']
        conclusion = details['conclusion']

        if isinstance(antecedents, list):
            for antecedent in antecedents:
                valeurs_regles.append(antecedent)
        else:
            valeurs_regles.append(antecedents)

        if isinstance(conclusion, list):
            for concl in conclusion:
                valeurs_regles.append(concl)
        else:
            valeurs_regles.append(conclusion)

    return valeurs_regles




####################################################################
def afficher_resultat():
    print('hello')
    matrice = matrice_entry.get()
    base_de_faits = build_base_de_faits(base_de_regles, matrice)
    regle_selectionnee = regle_combobox.get()
    print(matrice)
    print(base_de_faits)
    print(regle_selectionnee)
    if regle_selectionnee in base_de_regles:
        conclusion = base_de_regles[regle_selectionnee]['conclusion']

        resultat_text.delete(1.0, tk.END)
        resultat_text.insert(tk.END, f"Matrice carrée : {matrice}\n")
        resultat_text.insert(tk.END, f"Règle sélectionnée : {regle_selectionnee}\n")
        resultat_text.insert(tk.END, f"Conclusion : {conclusion}\n")

        # Vérification si la conclusion est déjà dans la base de faits
        if conclusion in base_de_faits:
            resultat_text.insert(tk.END, f"{conclusion} est déjà dans la base de faits.\n")
        else:
            resultat_text.insert(tk.END, f"{conclusion} n'est pas dans la base de faits. Chaînage en cours...\n")
            
            # Chaînage arrière
            objectif = conclusion
            regles = base_de_regles
            faits = base_de_faits.copy()  # Copie de la base de faits actuelle pour ne pas la modifier
            regles_utilisees = []  # Pour stocker les règles vraies utilisées
            while objectif not in faits:
                for regle, valeurs in regles.items():
                    if valeurs['conclusion'] == objectif:
                        antecedents = valeurs['antecedents']
                        tous_satisfaits = all(antecedent in faits for antecedent in antecedents)
                        if tous_satisfaits:
                            faits.append(objectif)
                            regles_utilisees.append(regle)
                            resultat_text.insert(tk.END, f"On peut utiliser la règle '{regle}' pour atteindre {objectif}.\n")
                            break

            if objectif in faits:
                resultat_text.insert(tk.END, f"Chaînage arrière terminé. {objectif} est maintenant dans la base de faits.\n")
                resultat_text.insert(tk.END, f"Les règles utilisées pour atteindre {objectif}: {', '.join(regles_utilisees)}\n")
            else:
                resultat_text.insert(tk.END, f"Chaînage arrière terminé. {objectif} n'a pas pu être prouvé.\n")



# Fonction pour le chaînage arrière
def chainer_arriere(objectif, regles, faits):
    if objectif in faits and faits[objectif]:
        return True  # L'objectif est atteint
    if objectif not in regles:
        return False  # L'objectif ne peut pas être atteint

    print(f"On suppose que {objectif}")
    regles_utilisees = []  # Pour stocker les règles vraies utilisées

    for regle, valeurs in regles.items():
        if valeurs['conclusion'] == objectif:
            antecedents = valeurs['antecedents']
            tous_satisfaits = all(faits[antecedent] for antecedent in antecedents)
            if tous_satisfaits:
                faits[objectif] = True
                regles_utilisees.append(regle)
                print(f"On peut utiliser la règle '{regle}' pour atteindre {objectif}.")

    if objectif in faits:
        print(f"Les règles utilisées pour atteindre {objectif}: {', '.join(regles_utilisees)}")
        return True  # L'objectif a été atteint

    return False  # Aucune règle ne peut atteindre l'objectif

################################################################################################

def build_base_de_faits(base_de_regles, matrice):
    base_de_faits = []
    valeurs_regles = extraire_valeurs(base_de_regles)

    for valeur in valeurs_regles:
        verifier_et_inserer(base_de_faits, matrice, valeur)

    return base_de_faits


##############################################################################################################################################################
# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("mathhelper")

# Champ d'entrée pour la matrice carrée
matrice_label = tk.Label(fenetre, text="Matrice carrée :")
matrice_label.pack()
matrice_entry = tk.Entry(fenetre)
matrice_entry.pack()

# Liste déroulante pour sélectionner une règle
regle_label = tk.Label(fenetre, text="Sélectionnez une règle :")
regle_label.pack()
regle_combobox = ttk.Combobox(fenetre, values=extraire_valeurs(base_de_regles))
regle_combobox.pack()

# Bouton pour afficher le résultat
afficher_button = tk.Button(fenetre, text="Afficher le résultat", command=afficher_resultat)
afficher_button.pack()

# Champ texte pour afficher le résultat
resultat_text = tk.Text(fenetre, height=50, width=40)
resultat_text.pack()

fenetre.mainloop()
