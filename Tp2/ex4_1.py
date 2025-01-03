# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex4_1.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ael-maaz <ael-maaz@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/03 20:31:39 by ael-maaz          #+#    #+#              #
#    Updated: 2025/01/03 20:38:23 by ael-maaz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:
	with open("fichier.txt", "w") as file:
		for i in range(1, 21):
			file.write(str(i))
		file.write("\n")
		for i in range(65, 91):
			file.write(chr(i))
except IOError as e:
	print(e)
except Exception as e:
	print(e)
