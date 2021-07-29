# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    state.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jiwhan <jiwhan@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/29 01:34:01 by jiwhan            #+#    #+#              #
#    Updated: 2021/07/29 02:26:31 by jiwhan           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def state(argv):
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
	state = argv[1]
	for i, j in capital_cities.items():
		if j == state:
			for k, w in states.items():
				if w == i:
					print(k)
					return
	print('Unknown capital city')

if __name__ == '__main__':
	state(sys.argv)