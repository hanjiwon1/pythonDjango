# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    var.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jiwhan <jiwhan@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/28 17:50:44 by jiwhan            #+#    #+#              #
#    Updated: 2021/07/29 21:13:13 by jiwhan           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def my_var():
	lst = [42, '42', 'quarante-deux', 42.0, True, [42], {42: 42}, (42,), set()]
	for i in lst:
		print(format(i) + ' has a type', type(i))

if __name__ == '__main__':
	my_var()
