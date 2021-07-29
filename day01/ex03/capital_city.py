# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    capital_city.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jiwhan <jiwhan@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/29 00:44:30 by jiwhan            #+#    #+#              #
#    Updated: 2021/07/29 01:18:00 by jiwhan           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def capital_city(argv):
	states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
	capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}
	if len(argv) != 2:
		return
	city = argv[1]
	if city in states:
		print(capital_cities[states[city]])
	else:
		print('Unknown state')

if __name__ == '__main__':
	capital_city(sys.argv)