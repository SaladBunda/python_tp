# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex5_2.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ael-maaz <ael-maaz@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/03 20:48:27 by ael-maaz          #+#    #+#              #
#    Updated: 2025/01/03 20:49:41 by ael-maaz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

# Spécifiez le chemin du dossier
dossier = "to_del"

try:
    # Liste tous les fichiers du dossier
    for fichier in os.listdir(dossier):
        chemin_complet = os.path.join(dossier, fichier)
        # Vérifie si c'est un fichier avant de le supprimer
        if os.path.isfile(chemin_complet):
            os.remove(chemin_complet)
            print(f"Fichier supprimé : {chemin_complet}")
except Exception as e:
    print(f"Erreur : {e}")
