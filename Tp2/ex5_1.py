# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex5_1.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ael-maaz <ael-maaz@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/01/03 20:42:04 by ael-maaz          #+#    #+#              #
#    Updated: 2025/01/03 20:45:46 by ael-maaz         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import csv

try:
	with open('exemple.csv', newline='', encoding='utf-8') as file:
		reader = csv.DictReader(file)  
		
		print(f"{'Col1':<10} {'Col2':<5} {'Col3':<15}")  
		print("-" * 35)  
		
		for row in reader:

			print(f"{row['Col1']:<10} {row['Col2']:<5} {row['Col3']:<15}")
except IOError as e:
	print(e)
except Exception as e:
	print(e)