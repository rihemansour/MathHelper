import numpy as np  # Vous pouvez utiliser NumPy pour effectuer des opérations sur les matrices

base_de_faits = []
def verifier_et_inserer(base_de_faits, matrice, proposition):
    if isinstance(matrice, str):
        matrice = np.array(eval(matrice))
    if proposition == 'Une matrice A est symétrique':
        if est_symetrique(matrice):
            base_de_faits.append(proposition)
    
    if proposition == 'Une matrice carrée A a un déterminant non nul':
        if calculer_determinant(matrice) != 0:
            base_de_faits.append(proposition)
    
    if proposition == 'Une matrice A est échelonnée':
        if est_echelonnee(matrice):
            base_de_faits.append(proposition)

    if proposition == 'Une matrice A est triangulaire supérieure':
        if est_triangulaire_superieure(matrice):
            base_de_faits.append(proposition)

# Vérification de la symétrie d'une matrice
def est_symetrique(matrice):
    return (matrice == matrice.T).all()

# Calcul du déterminant d'une matrice
def calculer_determinant(matrice):
    if matrice.shape[0] != matrice.shape[1]:
        return None  # La matrice n'est pas carrée, le déterminant n'existe pas
    return np.linalg.det(matrice)

# Vérification de l'échelonnage d'une matrice
def est_echelonnee(matrice):
    row, col = matrice.shape
    previous_pivot = -1
    for r in range(row):
        for c in range(col):
            if matrice[r, c] != 0:
                if c <= previous_pivot:
                    return False  # Le pivot actuel est à gauche ou sur la colonne du pivot précédent
                previous_pivot = c
                break
    return True

# Vérification de la matrice triangulaire supérieure
def est_triangulaire_superieure(matrice):
    row, col = matrice.shape
    for r in range(row):
        for c in range(r):
            if matrice[r, c] != 0:
                return False  # Il y a un élément non nul en dessous de la diagonale
    return True
