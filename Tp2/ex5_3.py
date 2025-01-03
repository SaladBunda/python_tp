# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex5_3.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ael-maaz <ael-maaz@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/03 20:51:19 by ael-maaz          #+#    #+#              #
#    Updated: 2025/01/03 20:55:15 by ael-maaz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

fichier = "exemple.txt"
mot_cle = "abcd"

with open(fichier, "r") as file:
	for line in file:
		if(line.find(mot_cle) != -1):
			print(line, end="")