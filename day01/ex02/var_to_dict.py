# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var_to_dict.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jiwhan <jiwhan@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/28 23:03:05 by jiwhan            #+#    #+#              #
#    Updated: 2021/07/29 00:46:23 by jiwhan           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def var_to_dict():
	d = [
('Hendrix' , '1942'),
('Allman' , '1946'),
('King' , '1925'),
('Clapton' , '1945'),
('Johnson' , '1911'),
('Berry' , '1926'),
('Vaughan' , '1954'),
('Cooder' , '1947'),
('Page' , '1944'),
('Richards' , '1943'),
('Hammett' , '1962'),
('Cobain' , '1967'),
('Garcia' , '1942'),
('Beck' , '1944'),
('Santana' , '1947'),
('Ramone' , '1948'),
('White' , '1975'),
('Frusciante', '1970'),
('Thompson' , '1949'),
('Burton' , '1939')
]

	dic = dict(d)
	dic = dict(zip(dic.values(), dic.keys()))
	for i, j in dic.items():
		print('{i} : {j}'.format(i=i, j=j))

if __name__ == '__main__':
	var_to_dict()