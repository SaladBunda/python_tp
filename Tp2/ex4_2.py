# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex4_2.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ael-maaz <ael-maaz@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/03 20:39:52 by ael-maaz          #+#    #+#              #
#    Updated: 2025/01/03 20:40:05 by ael-maaz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:
	with open('fichier.txt', 'r') as file:
		print(file.read())
except IOError as e:
	print(e)
except Exception as e:
	print(e)
