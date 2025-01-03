# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex4_3.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ael-maaz <ael-maaz@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/03 20:40:10 by ael-maaz          #+#    #+#              #
#    Updated: 2025/01/03 20:40:23 by ael-maaz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


try:
	with open("fichier.txt", "r") as file:
		with open("fichier2.txt", "w") as file2:
			file2.write(file.read())
except IOError as e:
	print(e)
except Exception as e:
	print(e)
