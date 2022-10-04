#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:37:30 2022

@author: colasnaudi
@author: mathisheriveau
"""
import pandas as pd
import matplotlib.pyplot as plt

# Import des fichiers
fic_accident = pd.read_table(
        "FichiersCSV/MAccident.csv",
        decimal = ",",
        sep = ","
)

fic_cause = pd.read_table(
        "FichiersCSV/MCause.csv",
        decimal = ",",
        sep = ","
)

fic_date = pd.read_table(
        "FichiersCSV/MDate.csv",
        decimal = ",",
        sep = ","
)

fic_etatSurface = pd.read_table(
        "FichiersCSV/MEtatSurface.csv",
        decimal = ",",
        sep = ","
)

fic_implique = pd.read_table(
        "FichiersCSV/MImplique.csv",
        decimal = ",",
        sep = ","
)

fic_intemperie = pd.read_table(
        "FichiersCSV/MIntemperie.csv",
        decimal = ",",
        sep = ","
)

fic_lieu = pd.read_table(
        "FichiersCSV/MLieu.csv",
        decimal = ",",
        sep = ","
)

fic_luminosite = pd.read_table(
        "FichiersCSV/MLuminosite.csv",
        decimal = ",",
        sep = ","
)

fic_etatSurface = pd.read_table(
        "FichiersCSV/MTypeEtatSurface.csv",
        decimal = ",",
        sep = ","
)

fic_typeImplication = pd.read_table(
        "FichiersCSV/MTypeImplication.csv",
        decimal = ",",
        sep = ","
)

# ~~~~~~~~ Tableau contenant id_accident, libelle_cause, date_accident ~~~~~~~ #
# ~~~~~~~~~ qui contient uniquement les accidents liés à l'ivresse ~~~~~~~~~~~ #


accident_ivresse = fic_accident.merge(fic_date, how="left", on="date_id")
accident_ivresse = accident_ivresse.merge(fic_cause, left_on='cause_id', right_on='Cause', suffixes=(False, False))
accident_ivresse = accident_ivresse.sort_values('cause_id')
accident_ivresse = accident_ivresse.iloc[:,[0,3,11,16]]
copy = accident_ivresse.copy()


corresp = {'Ecart sur le côté' : 'Autre', 
           'Tourne à gauche interdit' : 'Autre', 
           'Dépassement en 3eme position' : 'Autre', 
           'Défaut de maîtrise' : 'Autre', 
           'Heurte véhicule en stationnement interdit' : 'Autre', 
           'Entre sur la chaussée' : 'Autre', 
           'Mauvais positionnement (chgt de file)' : 'Autre', 
           'Non respect priorité a droite (avec feux clignotant)' : 'Autre', 
           'non respect du stop' : 'Autre', 
           'non respect feux tricolores' : 'Autre', 
           'Eblouissement par les phares' : 'Autre', 
           'Va stationner a gauche' : 'Autre', 
           'Joue ou travaille sur la chaussée' : 'Autre', 
           'Roule en marche arrière' : 'Autre', 
           'Traverse hors passage': 'Autre', 
           'Heurte un obstacle mobile' : 'Autre', 
           'Tourne à droite interdit' : 'Autre', 
           'Incident mécanique' : 'Autre', 
           'Non respect du piéton en carrefour': 'Autre', 
           'Heurte un obstacle inerte' : 'Autre', 
           'Marche arrière pour stationner' : 'Autre', 
           'Dépassement en virage' : 'Autre', 
           'Demi-tour' : 'Autre', 
           'non respect des signaux' : 'Autre', 
           'Non respect du piéton en section' : 'Autre', 
           'Dépassement en carrefour' : 'Autre', 
           'Dépassement dangereux' : 'Autre', 
           "Piéton descendant d'un t.c." : 'Autre', 
           'Marche sur la chaussée' : 'Autre', 
           'Queue de poisson' : 'Autre', 
           'Manoeuvre sur parking' : 'Autre', 
           'Indéterminée' : 'Autre', 
           'Malaise' : 'Autre', 
           'Non respect priorité a droite' : 'Autre', 
           'Roule à gauche' : 'Autre', 
           'Circule sur le trottoir' : 'Autre', 
           'Heurte un véhicule en stationnement' : 'Autre', 
           'Dépassement a droite' : 'Autre', 
           'Quitte le stationnement' : 'Autre', 
           "Ouverture d'une portière" : 'Autre', 
           'Piéton montant dans un t.c.' : 'Autre', 
           'Ivresse' : 'Ivresse', 
           'Perte de contrôle' : 'Autre', 
           'Non respect priorité de face' : 'Autre', 
           'Eclairage insuffisant du véhicule' : 'Autre', 
           'Sens interdit' : 'Autre', 
           "Non respect d'une balise" : 'Autre', 
           'Traverse sans précaution' : 'Autre', 
           'Entre ou sort de véhicule en stationnement' : 'Autre'
}

accident_ivresse['libelle'] = accident_ivresse['libelle'].map(corresp)

plots = pd.crosstab(accident_ivresse['libelle'], accident_ivresse['gravite'], normalize="index")


plots.plot(
    kind="bar",
    stacked=True,
)



plt.xticks(rotation=70)
plt.xlabel('')
plt.legend(['Aucune gravité','Gravité légére','Grave','Très grave'],bbox_to_anchor =(1, 1), ncol = 1)

plt.title("Gravité des accidents en fonction de leurs causes")

plt.show()