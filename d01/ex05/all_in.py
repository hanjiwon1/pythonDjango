# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    all_in.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jiwhan <jiwhan@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/29 02:32:34 by jiwhan            #+#    #+#              #
#    Updated: 2021/07/29 16:03:04 by jiwhan           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def split_str(s):
	s = list(map(str, s.split(',')))
	ret = []
	for i in range(len(s)):
		if len(s[i].strip())>0:
			ret.append(((s[i].strip()).lower()).title())
	return ret

def all_in(argv):
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
	input_cities = split_str(argv[1])
	capital_cities_rev = dict(zip(capital_cities.values(), capital_cities.keys()))
	states_rev = dict(zip(states.values(), states.keys()))

	for i in input_cities:
		if i in capital_cities_rev:
			print("{i} is the capital of {j}".format(i = i, j = states_rev[capital_cities_rev[i]]))

		elif i in states.keys():
			print("{j} is the capital of {i}".format(j = capital_cities[states[i]], i = i))

		else:
			print("{i} is neither a capital city nor a state".format(i = i))

if __name__ == '__main__':
	all_in(sys.argv)