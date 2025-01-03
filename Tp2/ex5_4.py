# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex5_4.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ael-maaz <ael-maaz@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/03 20:56:17 by ael-maaz          #+#    #+#              #
#    Updated: 2025/01/03 20:56:18 by ael-maaz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import logging

# Configurer le fichier journal
logging.basicConfig(
    filename="programme.log",  # Nom du fichier journal
    level=logging.INFO,        # Niveau de journalisation (INFO, DEBUG, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format des messages
    filemode="a",              # Mode 'a' pour ajouter au fichier existant ou 'w' pour écraser
)

# Exemple d'utilisation
logging.info("Programme démarré.")
logging.debug("Ceci est un message de débogage.")
logging.warning("Ceci est un avertissement.")
logging.error("Une erreur est survenue.")
logging.critical("Problème critique rencontré.")
logging.info("Programme terminé.")
