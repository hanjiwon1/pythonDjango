# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    periodic_table.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jiwhan <jiwhan@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/29 16:50:35 by jiwhan            #+#    #+#              #
#    Updated: 2021/07/29 20:26:01 by jiwhan           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def read_txt():
	r = open('periodic_table.txt', 'r')
	l = r.read().split('\n')
	element_list = []
	for i in l:
		if len(i) == 0:
			break
		temp = i.split(',')
		name = ((temp[0].split('='))[0]).strip()
		position = int((temp[0].split(':'))[1])
		number = int(temp[1].split(':')[1])
		small = temp[2].split(': ')[1]
		molar = float(temp[3].split(':')[1])
		electron = list(map(int, (temp[4].split(':')[1]).split(' ')))
		element_list.append([name, position, number, small, molar, electron])
	r.close()
	return element_list

def create_html(element):
	f = open('periodic_table.html', 'w')
	head = """<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<table style="border: 1px solid black; padding:10px">
		<thead>
			<tr>
				<th colspan="18">The Mendeleev's table</th>
			</tr>
		</thead>
		<tbody>"""
	f.write(head)
	k = 0
	for i in range(7):
		f.write("""<tr>""")
		for j in range(18):
			if element[k][1] == j:
				f.write("""<td style="border: 1px solid black; padding:10px;"><h4>{name}</h4><ul><li>No {number}</li><li>{small}</li><li>{molar}</li><li>{electron} electron</li></ul></td>""".format(name = element[k][0], number = element[k][2], small = element[k][3], molar = element[k][4], electron = element[k][5]))
				k = k+1
			else:
				f.write("""<td style="border: 1px solid black; padding:10px"></td>""")
		f.write("""</tr>""")
	f.write("""</tbody></table></body></html>""")
	f.close()

def create_table():
	table_elem = read_txt()
	for i in table_elem:
		create_html(table_elem)

if __name__ == '__main__':
	create_table()