# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    render.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jiwhan <jiwhan@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/30 14:49:46 by jiwhan            #+#    #+#              #
#    Updated: 2021/07/30 16:09:20 by jiwhan           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import os
from settings import *

def render(file_name):
	if len(file_name) != 2:
		sys.exit("wrong number of arguments")
	if os.path.isfile(file_name[1]) == False:
		sys.exit('non existing file')
	fname, ext = os.path.splitext(file_name[1])
	if ext != ".template":
		sys.exit('wrong file extension')
	cv = open(file_name[1], 'r')
	script = cv.read()
	cv.close()
	f_html = open("{fname}.html".format(fname = fname), "w")
	f_html.write(script.format(title = title, name = name, surname = surname, age = age, profession = profession))
	f_html.close()
	print(globals())

if __name__ == '__main__':
	render(sys.argv)