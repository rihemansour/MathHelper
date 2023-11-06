import tkinter as tk
import numpy as np
from tkinter import ttk

# Define the base of rules and facts
base_de_regles = {
    'regle1': {'antecedents': ['A a un déterminant non nul'], 'conclusion': 'A est inversible'},
    'regle2': {'antecedents': ['A est inversible'], 'conclusion': 'L\'inverse de A est unique'},
    'regle3': {'antecedents': ['A est symétrique', 'A est inversible'], 'conclusion': 'L\'inverse de A est également symétrique'},
    'regle4': {'antecedents': ['A est diagonale'], 'conclusion': 'La matrice A est inversible si et seulement si tous les éléments diagonaux sont non nuls'},
    'regle5': {'antecedents': ['A est échelonnée'], 'conclusion': 'A est inversible si tous les pivots sont non nuls'},
    'regle6': {'antecedents': ['A est inversible'], 'conclusion': 'Le transposé de A est inversible'},
    'regle7': {'antecedents': ['A est triangulaire supérieure', 'A est inversible'], 'conclusion': 'A est diagonale'},
    'regle8': {'antecedents': ['A a un déterminant non nul'], 'conclusion': 'A est inversible'},
    'regle9': {'antecedents': ['A est inversible', 'A est symétrique'], 'conclusion': 'A est diagonalisable'},
    'regle10': {'antecedents': ['A est échelonnée', 'A est diagonale'], 'conclusion': 'A est une matrice identité'},
    'regle11': {'antecedents': ['A est diagonalisable', 'A est symétrique'], 'conclusion': 'A est une matrice orthogonale'},
    'regle12': {'antecedents': ['A est inversible', 'A est une matrice identité'], 'conclusion': 'A est une matrice de permutation'}
}


# Create an empty list for facts
base_de_faits = []
propositions =[]
for regle in base_de_regles.values():
    propositions.append(regle['conclusion'])
    propositions.extend(regle['antecedents'])
ensemble_sans_redondance = set(propositions)
propositions = list(ensemble_sans_redondance)
# Function to check and insert facts into the base_de_faits
# Function to check and insert facts into the base_de_faits
def verifier_et_inserer(matrice, proposition):
    global base_de_faits  # Indique que vous utilisez la variable globale

    if isinstance(matrice, str):
        matrice = np.array(eval(matrice))
    
    faits_ajoutes = []  # Créez une liste pour stocker les faits ajoutés

    if proposition == 'A est symétrique':
        if est_symetrique(matrice):
            faits_ajoutes.append(proposition)
            print(f'Fact ajouté: {proposition}')
    
    if proposition == 'A a un déterminant non nul':
        if calculer_determinant(matrice) != 0:
            faits_ajoutes.append(proposition)
            print(f'Fact ajouté: {proposition}')
    
    if proposition == 'A est échelonnée':
        if est_echelonnee(matrice):
            faits_ajoutes.append(proposition)
            print(f'Fact ajouté: {proposition}')
    
    if proposition == 'A est triangulaire supérieure':
        if est_triangulaire_superieure(matrice):
            faits_ajoutes.append(proposition)
            print(f'Fact ajouté: {proposition}')
    
    if proposition == 'Le déterminant de A est non nul':
        if calculer_determinant(matrice) != 0:
            faits_ajoutes.append(proposition)
            print(f'Fact ajouté: {proposition}')
    
    # Nouvelles propositions
    if proposition == 'A est inversible':
        if est_inversible(matrice):
            faits_ajoutes.append(proposition)
            print(f'Fact ajouté: {proposition}')
    
    if proposition == 'L\'inverse de A est unique':
        if inverse_unique(matrice):
            faits_ajoutes.append(proposition)
            print(f'Fact ajouté: {proposition}')
    
    if proposition == 'L\'inverse de A est également symétrique':
        if inverse_symetrique(matrice):
            faits_ajoutes.append(proposition)
            print(f'Fact ajouté: {proposition}')
    
    if proposition == 'A est diagonalisable':
        if est_diagonalisable(matrice):
            faits_ajoutes.append(proposition)
            print(f'Fact ajouté: {proposition}')
    
    if proposition == 'A est une matrice identité':
        if est_matrice_identite(matrice):
            faits_ajoutes.append(proposition)
            print(f'Fact ajouté: {proposition}')
    
    if proposition == 'A est une matrice orthogonale':
        if est_matrice_orthogonale(matrice):
            faits_ajoutes.append(proposition)
            print(f'Fact ajouté: {proposition}')
    
    if proposition == 'A est une matrice de permutation':
        if est_matrice_permutation(matrice):
            faits_ajoutes.append(proposition)
            print(f'Fact ajouté: {proposition}')

    # Mettez à jour la base de faits en ajoutant les faits vérifiés
    base_de_faits.extend(faits_ajoutes)
# Fonction pour vérifier si une matrice est inversible
def est_inversible(matrice):
    return calculer_determinant(matrice) != 0

# Fonction pour vérifier si l'inverse d'une matrice est unique
def inverse_unique(matrice):
    # L'inverse est unique si le déterminant est non nul
    return calculer_determinant(matrice) != 0

# Fonction pour vérifier si l'inverse d'une matrice est également symétrique
def inverse_symetrique(matrice):
    # Pour la symétrie de l'inverse, nous allons simplement vérifier si l'inverse est symétrique
    return est_symetrique(np.linalg.inv(matrice))

# Fonction pour vérifier si une matrice est diagonalisable
def est_diagonalisable(matrice):
    # La diagonalisation dépend de la nature de la matrice, vérifiez si elle est diagonalisable
    # Par exemple, pour une matrice carrée, vérifiez si elle est diagonalisable.
    return np.all(np.iscomplex(np.linalg.eigvals(matrice)))  # Utilisation d'une propriété basique ici

# Fonction pour vérifier si une matrice est une matrice identité
def est_matrice_identite(matrice):
    return np.array_equal(matrice, np.eye(matrice.shape[0]))

# Fonction pour vérifier si une matrice est une matrice orthogonale
def est_matrice_orthogonale(matrice):
    # Une matrice est orthogonale si son inverse est égal à sa transposée
    return np.array_equal(np.linalg.inv(matrice), matrice.T)

# Fonction pour vérifier si une matrice est une matrice de permutation
def est_matrice_permutation(matrice):
    # Une matrice de permutation a une somme des éléments égale à 1 par ligne/colonne
    return np.all(np.sum(matrice, axis=1) == 1) and np.all(np.sum(matrice, axis=0) == 1)


# Function to check if a matrix is symmetric
def est_symetrique(matrice):
    return (matrice == matrice.T).all()

# Function to calculate the determinant of a matrix
def calculer_determinant(matrice):
    if matrice.shape[0] != matrice.shape[1]:
        return None  # The matrix is not square, so the determinant does not exist
    return np.linalg.det(matrice)

# Function to check if a matrix is in echelon form
def est_echelonnee(matrice):
    row, col = matrice.shape
    previous_pivot = -1
    for r in range(row):
        for c in range(col):
            if matrice[r, c] != 0:
                if c <= previous_pivot:
                    return False  # The current pivot is to the left or on the column of the previous pivot
                previous_pivot = c
                break
    return True

# Function to check if a matrix is upper triangular
def est_triangulaire_superieure(matrice):
    row, col = matrice.shape
    for r in range(row):
        for c in range(r):
            if matrice[r, c] != 0:
                return False  # There is a non-zero element below the diagonal
    return True

# Function to build the base of facts
def build_base_de_faits(matrice):
    global base_de_faits  # Indique que vous utilisez la variable globale
    verifier_et_inserer(matrice, 'A est symétrique')
    verifier_et_inserer(matrice, 'A a un déterminant non nul')
    verifier_et_inserer(matrice, 'A est échelonnée')
    verifier_et_inserer(matrice, 'A est triangulaire supérieure')
    verifier_et_inserer(matrice, 'Le déterminant de A est non nul')


# Function to prove a proposition
def prouver_proposition(prop, base_de_regles, base_de_faits, regles_utilisees):
    if prop in base_de_faits:
        return True
    if prop not in base_de_regles:
        return False

    regle = None
    for r, details in base_de_regles.items():
        if details['conclusion'] == prop:
            regle = r
            break

    if regle is not None:
        antecedents = base_de_regles[regle]['antecedents']
        antecedents_prouves = all(prouver_proposition(ant, base_de_regles, base_de_faits, regles_utilisees) for ant in antecedents)
        if antecedents_prouves:
            verifier_et_inserer(matrice_entry.get(), prop)
            regles_utilisees.append(regle)
            return True
    return False

# Function for backward chaining
# Function for backward chaining
def chainer_arriere(objectif, base_de_regles, base_de_faits):
    print(f"Chercher à prouver : {objectif}")
    
    if objectif in base_de_faits:
        resultat_text.insert(tk.END, f"{objectif} est déjà dans la base de faits.\n")

        return True, []
    
    if objectif not in propositions:
        resultat_text.insert(tk.END, f"{objectif} n'est pas une conclusion dans les règles.\n")
        return False, []
    
    regles_utilisees = []
    
    print("Commencer la recherche des règles pour prouver :", objectif)
    
    for regle, details in base_de_regles.items():
        if details['conclusion'] == objectif:
            resultat_text.insert(tk.END, f"Vérification de la règle : {regle}\n")

            antecedents = details['antecedents']
            antecedents_prouves = []
            
            for ant in antecedents:
                resultat, regles_antecedent = chainer_arriere(ant, base_de_regles, base_de_faits)
                antecedents_prouves.append(resultat)
                regles_utilisees += regles_antecedent
            
            if all(antecedents_prouves):
                resultat_text.insert(tk.END, f"La règle {regle} a été prouvée.\n")

                verifier_et_inserer(matrice_entry.get(), objectif)
                regles_utilisees.append(regle)
                return True, regles_utilisees
            else:
                resultat_text.insert(tk.END, f"La règle {regle} n'a pas pu être prouvée.\n")
    
    print(f"Impossible de prouver : {objectif}")
    return False, regles_utilisees

# Function to display the result
def afficher_resultat():
    
    global base_de_faits
    matrice = matrice_entry.get()
    proposition_selectionnee = regle_combobox.get()
    resultat_text.delete(1.0, tk.END)
    resultat_text.insert(tk.END, "***************************REGLES***************************\n")

    # Display the list of rules
    for regle, details in base_de_regles.items():
        resultat_text.insert(tk.END, f"Règle {regle} : Si {', '.join(details['antecedents'])}, alors {details['conclusion']}.\n")
    resultat_text.insert(tk.END, "************************************************************\n")
    resultat_text.insert(tk.END, "\n")
    resultat_text.insert(tk.END, f"Matrice carrée : {matrice}\n")
    build_base_de_faits(matrice)
    print(f'Base de faits: {base_de_faits}')

    if proposition_selectionnee:
        resultat_text.insert(tk.END, f"Proposition sélectionnée : {proposition_selectionnee}\n")
        preuve, regles_utilisees = chainer_arriere(proposition_selectionnee, base_de_regles, base_de_faits)
        if regles_utilisees !=[]:
            resultat_text.insert(tk.END, f"Règles utilisées : {', '.join(regles_utilisees)}\n")
        if preuve:
            resultat_text.insert(tk.END, f"{proposition_selectionnee} a été prouvé.\n")
        else:
            resultat_text.insert(tk.END, f"{proposition_selectionnee} ne peut pas être prouvé et donc n'est pas vérifiée par la matrice donnée.\n")
    else:
        resultat_text.insert(tk.END, "Sélectionnez une proposition avant d'afficher le résultat.\n")
    base_de_faits = []
    resultat_text.insert(tk.END, "************************************************************\n")
# Create the window
fenetre = tk.Tk()
fenetre.title("mathhelper")

# Entry field for the square matrix
matrice_label = tk.Label(fenetre, text="Matrice carrée :")
matrice_label.pack()
matrice_entry = tk.Entry(fenetre,width=60)
matrice_entry.pack()

# Combobox to select a proposition




regle_label = tk.Label(fenetre, text="Sélectionnez une proposition :")
regle_label.pack()
regle_combobox = ttk.Combobox(fenetre, values=propositions,width= 60)
regle_combobox.pack()

# Button to display the result
afficher_button = tk.Button(fenetre, text="Afficher le résultat", command=afficher_resultat)
afficher_button.pack()

# Text field to display the result
resultat_text = tk.Text(fenetre, height=20, width=60)
resultat_text.pack()

fenetre.mainloop()
