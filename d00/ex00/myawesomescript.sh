# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    myawesomescript.sh                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jiwhan <jiwhan@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/07/26 19:17:14 by jiwhan            #+#    #+#              #
#    Updated: 2021/07/28 15:45:21 by jiwhan           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/sh

curl -s $1 | grep 'href' | cut -f2 -d '"'
